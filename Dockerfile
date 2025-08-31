FROM docker.io/nginx:latest
# Unfortunately this assumes we have run `npm run build` outside of docker...
# TODO Run all required build steps inside the Dockerfile
COPY dist/ /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/nginx.conf