FROM python:latest AS rootbuilder
WORKDIR /workdir
ARG COMMIT_SHA="yeetuscommitus"
RUN --mount=type=bind,target=/workdir python3 -m pip install markdown && \
    python3 buildblog.py --output /tmp/dynamic-root --commit $COMMIT_SHA

FROM docker.io/nginx:latest
COPY --from=rootbuilder /tmp/dynamic-root/ /usr/share/nginx/html
COPY root/* /usr/share/nginx/html/
