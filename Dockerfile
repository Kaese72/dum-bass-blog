FROM docker.io/nginx:latest
ARG COMMIT_SHA="yeetuscommitus"
COPY ./root /usr/share/nginx/html
RUN sed -i "s/GITHUB_COMMIT_HASH/$COMMIT_SHA/g" /usr/share/nginx/html/index.html
