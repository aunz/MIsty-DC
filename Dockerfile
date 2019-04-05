FROM node:11-alpine

RUN apk add --update  python3-dev build-base openblas-dev libexecinfo-dev

RUN mkdir -p /app/python
RUN mkdir -p /app/node

COPY python/requirements.txt /app/python
WORKDIR /app/python
RUN pip3 install -r requirements.txt

COPY node/package.json /app/node
WORKDIR /app/node
RUN npm install

COPY python/. /app/python
COPY node/index.js /app/node

WORKDIR /app

EXPOSE 3000

CMD ['node', 'node/index', '&', 'python3', 'python/server.py', '&']