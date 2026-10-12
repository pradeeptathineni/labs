// web/main.jsx - Add notes through the proxy and show saved titles

// Use React for the small form and list
import React, {useEffect, useState} from 'react';
import {createRoot} from 'react-dom/client';

// Keep form state and request failures visible
function App() {
    const [notes, setNotes] = useState([]);
    const [title, setTitle] = useState('');
    const [error, setError] = useState('');

    // Load the saved list and check HTTP failures
    async function load() {
        const response = await fetch('/api/notes');
        if (!response.ok) throw new Error('Could not load notes');
        setNotes(await response.json());
    }
    useEffect(() => {load().catch(e => setError(e.message));}, []);

    // Save the entered note, then refresh the list
    async function save(event) {
        event.preventDefault();
        setError('');
        try {
            const response = await fetch('/api/notes', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({title})
            });
            if (!response.ok) throw new Error('Could not save note');
            setTitle('');
            await load();
        } catch (e) {
            setError(e.message);
        }
    }

    // Render escaped titles with a named input and an announced error
    return <main>
        <h1>Lab notes</h1>
        <form onSubmit={save}>
            <label htmlFor="title">New note </label>
            <input id="title" value={title} maxLength={200} required
                onChange={event => setTitle(event.target.value)} />
            <button>Save</button>
        </form>
        <p role="alert">{error}</p>
        <ul>{notes.map((note, i) => <li key={i}>{note.title}</li>)}</ul>
    </main>;
}

// Attach the app to the page
createRoot(document.getElementById('root')).render(<App />);
