# purpose of this project
Some sites like Microsoft or Jfrog have rich documentation to offer online, the issue is with on premise environments where the documentation is not available.
This project will take the pdf of the documentation and create a containerized website powered by Docusaurus that you would be able to host in your on premise environment. 

Powered by [docusaurus](https://docusaurus.io/docs)

# How to develop
## Requirements
- Node.js version 16.14 or above (according to https://docusaurus.io/docs/installation)
## Set up dev server
Download the latest version of docusaurus:
```sh
npx create-docusaurus@latest my-website classic
```
Run your website
```sh
cd my-website
npm run start 
```
By default, a browser window will open at http://localhost:3000.