FROM node:18.5.0-alpine

# Install react packages
COPY ./src/frontend/package.json ./src/frontend/yarn.lock ./
RUN yarn install --network-timeout 100000

# Copy source
COPY ./src/frontend .