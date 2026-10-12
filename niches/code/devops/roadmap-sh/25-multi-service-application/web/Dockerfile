# web/Dockerfile - Build React and keep only its output in the final image
FROM labs-notes-web-base:local AS build

# Build the page with the custom Node base
COPY index.html main.jsx ./
RUN npm run build

# Serve the built files without shipping Node or build packages
FROM nginx:1.28-alpine@sha256:a8b39bd9cf0f83869a2162827a0caf6137ddf759d50a171451b335cecc87d236
COPY --from=build /app/dist /usr/share/nginx/html
