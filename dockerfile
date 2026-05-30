FROM node:22.18.0-alpine3.21

WORKDIR /app

COPY package.json pnpm-lock.yaml* ./
COPY tsconfig*.json ./
RUN corepack enable pnpm && pnpm install
COPY . .

EXPOSE 3000

ENV HOST=0.0.0.0
CMD ["pnpm", "run", "dev"]