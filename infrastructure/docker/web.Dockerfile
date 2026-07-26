FROM node:22-alpine AS dependencies

RUN corepack enable
WORKDIR /app

COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
COPY apps/web/package.json apps/web/package.json
COPY packages/api-contracts/package.json packages/api-contracts/package.json
RUN pnpm install --frozen-lockfile

FROM dependencies AS builder
COPY apps/web apps/web
COPY packages/api-contracts packages/api-contracts
RUN pnpm --filter @equity-research/web build

FROM node:22-alpine AS runner
ENV NODE_ENV=production \
    HOSTNAME=0.0.0.0 \
    PORT=3000
WORKDIR /app

COPY --from=builder /app/apps/web/.next/standalone ./
COPY --from=builder /app/apps/web/.next/static ./apps/web/.next/static
COPY --from=builder /app/apps/web/public ./apps/web/public

EXPOSE 3000

CMD ["node", "apps/web/server.js"]
