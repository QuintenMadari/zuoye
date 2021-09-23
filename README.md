# Quick blog with hugo & book theme using submodules

## general 

1. Install hugo (on termux in my case)
2. create 2 repos, 1 for code, 1 more for md collab, could create 1 for deployment but overkill
3. go to https://themes.gohugo.io/ and select a theme. each theme works a bit different
  - book theme is best
4. in code repo, hugo new site, apply theme submodule
  - in my case 
    git submodule add https://github.com/alex-shpak/hugo-book themes/book
5. in theme/book/exampleSite find config.toml and edit as desired. copy to root folder
6. exit, check if it runs locally by running hugo server (localhost:1313)
  - it does! not on duckduckgobrowser use 127.0.0.1 instead of localhost
7. (optional) in root folder of code repo, git submodule add -b main [url] public
  - git submodule add -b main git@github.com:QuintenMadari/deploymentcodeonly public
8. In code repo, hugo new docs/post.md makes file with boilerplate, manually is fine too
  > By default, the theme will render pages from the content/docs section as a menu in a tree structure.
  > You can set title and weight in the front matter of pages to adjust the order and titles in the menu
9. root folder code repo, hugo -t book, to create static files in public folder

## submodules

By turning the content folders (content and content.py in this case) into 
