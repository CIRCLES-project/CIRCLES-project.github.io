FROM golang:1.22-alpine

RUN apk add zola --repository=https://dl-cdn.alpinelinux.org/alpine/edge/community

# hugo provided
LABEL LICENSE="MIT"
LABEL LICENSE_URL="https://github.com/getzola/zola/blob/master/LICENSE"

RUN apk add --no-cache bash git nodejs npm

# Cloudflare Wrangler provided under MIT
LABEL LICENSE="MIT"
LABEL LICENSE_URL="https://github.com/cloudflare/workers-sdk/blob/main/LICENSE-MIT"

RUN npm install -g wrangler@3.60.2
