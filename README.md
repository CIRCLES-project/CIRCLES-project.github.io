# Circles Marketing Site

## Getting Started

Get the theme submodule

`git submodule update --init --recursive`

Install [Zola](https://www.getzola.org/documentation/getting-started/installation/https://www.getzola.org/documentation/getting-started/installation/)

## Generate a site

`zola build`

this creates a ./public directory containing site

## Site live preview

`zola serve`

`Web server is available at http://127.0.0.1:1111/ (bound to 127.0.0.1:1111)`

Open web site in local browser, view and edit!

## Deployment

requires Cloudflare Wrangler & node,npm

``` sh
zola build
wrangler pages deploy --project-name circles-futo-org ./public
```