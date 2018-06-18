FROM raseel/ubuntu16-node
MAINTAINER Raseel Bhagat <raseelbhagat@gmail.com>

RUN mkdir -p /web-client
COPY src /web-client/src

COPY angular.json /web-client/angular.json
COPY package.json /web-client/package.json
COPY tsconfig.json /web-client/tsconfig.json
COPY tslint.json /web-client/tslint.json
COPY entrypoint.sh /entrypoint.sh

WORKDIR /web-client
RUN npm install

EXPOSE 4200

ENTRYPOINT [ "/entrypoint.sh" ]