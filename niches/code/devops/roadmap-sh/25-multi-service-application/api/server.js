// api/server.js - Store notes and cache the list

// Read the password file and use the existing database clients
import {readFileSync} from 'node:fs';
import express from 'express';
import {MongoClient} from 'mongodb';
import {createClient} from 'redis';

// Keep passwords out of image layers and environment values
const password = readFileSync('/run/secrets/mongo_password', 'utf8').trim();
if (!password) throw new Error('Missing database password');
const mongo = new MongoClient(
    `mongodb://lab:${encodeURIComponent(password)}@mongo:27017/?authSource=admin`,
    {serverSelectionTimeoutMS: 1500}
);
const cache = createClient({
    url: 'redis://redis:6379',
    disableOfflineQueue: true,
    socket: {connectTimeout: 1500}
});
cache.on('error', () => console.error('Cache connection failed'));

// Connect before accepting requests
await mongo.connect();
await cache.connect();
const notes = mongo.db('notes').collection('notes');
const app = express();
app.disable('x-powered-by');
app.use(express.json({limit: '8kb'}));

// Report readiness only when both stores answer
app.get('/health', async (req, res) => {
    await mongo.db('admin').command({ping: 1});
    await cache.ping();
    res.json({ready: true});
});

// Reuse the list for a short time and show whether it came from the cache
app.get('/notes', async (req, res) => {
    const saved = await cache.get('notes');
    if (saved) return res.set('X-Cache', 'hit').json(JSON.parse(saved));
    const rows = await notes.find({}, {projection: {_id: 0}}).sort({time: 1}).toArray();
    await cache.set('notes', JSON.stringify(rows), {EX: 10});
    res.set('X-Cache', 'miss').json(rows);
});

// Reject bad input before writing, then clear the old cached list
app.post('/notes', async (req, res) => {
    const title = req.body?.title;
    if (typeof title !== 'string' || !title.trim() || title.length > 200) {
        return res.status(400).json({error: 'Use a title between 1 and 200 characters'});
    }
    await cache.ping();
    const note = {title: title.trim(), time: new Date().toISOString()};
    await notes.insertOne(note);
    await cache.del('notes');
    res.status(201).json(note);
});

// Keep bad JSON separate from a failed dependency without exposing credentials
app.use((error, req, res, next) => {
    const status = error.type === 'entity.parse.failed' ? 400
        : error.type === 'entity.too.large' ? 413 : 503;
    res.status(status).json({error: status === 503 ? 'Store unavailable' : 'Invalid JSON body'});
});

// Stop accepting requests before closing store connections
const server = app.listen(3000, '0.0.0.0');
async function stop() {
    server.close();
    await Promise.allSettled([mongo.close(), cache.quit()]);
    process.exit(0);
}
process.on('SIGTERM', stop);
process.on('SIGINT', stop);
