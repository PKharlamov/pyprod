FROM node:19.6-alpine as build-stage
WORKDIR /app
COPY package.json ./
RUN npm install
COPY ./ .
RUN npm run build

FROM nginx:1.23-alpine as production-stage
RUN mkdir /app
COPY --from=build-stage /app/dist /app
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 3000
