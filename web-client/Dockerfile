FROM raseel/ubuntu16-node as builder
MAINTAINER Raseel Bhagat <raseelbhagat@gmail.com>

RUN apt-get update && apt-get install -y --no-install-recommends nginx
RUN mkdir -p /web-client
COPY src /web-client/src

COPY angular.json /web-client/angular.json
COPY package.json /web-client/package.json
COPY tsconfig.json /web-client/tsconfig.json
COPY tslint.json /web-client/tslint.json

WORKDIR /web-client
RUN npm install && npm run build

# Final image
FROM nginx:latest
COPY --from=builder /web-client/dist/live-location-tracker/ /usr/share/nginx/html/
COPY ./llt.conf /etc/nginx/conf.d/default.conf

EXPOSE 80