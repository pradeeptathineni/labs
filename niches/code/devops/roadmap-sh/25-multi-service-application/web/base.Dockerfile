# web/base.Dockerfile - Shared Node build tools with locked web packages
FROM node:24-bookworm-slim@sha256:2fe369e969550cde8e867afc3fe370b260140cab4a23d467074295b42163d553

# Install build packages separately from application changes
WORKDIR /app
COPY package*.json ./
RUN npm ci && npm cache clean --force
