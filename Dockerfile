FROM python:latest AS rootbuilder
WORKDIR /workdir
RUN --mount=type=bind,target=/workdir python3 -m pip install markdown && \
    python3 buildblog.py --output /tmp/dynamic-root

FROM docker.io/nginx:latest
ARG COMMIT_SHA="yeetuscommitus"
COPY --from=rootbuilder /tmp/dynamic-root/ /usr/share/nginx/html
COPY root/* /usr/share/nginx/html/
RUN sed -i "s/GITHUB_COMMIT_HASH/$COMMIT_SHA/g" /usr/share/nginx/html/index.html
