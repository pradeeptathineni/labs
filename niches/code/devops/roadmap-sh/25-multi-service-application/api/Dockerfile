# api/Dockerfile - Run the notes API from its custom base image
FROM labs-notes-api-base:local

# Copy only the server and use a non-root runtime
COPY --chown=node:node server.js ./
EXPOSE 3000
CMD ["node", "server.js"]
