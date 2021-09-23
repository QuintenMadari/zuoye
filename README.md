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
  - changed folder structure of languages, made zh an py
  - content can now be a submodule
6. exit, check if it runs locally by running hugo server (localhost:1313)
  - it does! not on duckduckgobrowser use 127.0.0.1 instead of localhost
7. (optional) in root folder of code repo, git submodule add -b main [url] public
  - git submodule add -b main git@github.com:QuintenMadari/deploymentcodeonly public
8. In code repo, hugo new docs/post.md makes file with boilerplate, manually is fine too
  > By default, the theme will render pages from the content/docs section as a menu in a tree structure.
  > You can set title and weight in the front matter of pages to adjust the order and titles in the menu
9. root folder code repo, hugo -t book, to create static files in public folder

## submodules

1. do a touch readme.md git add . commit push action to the post collab repo
2. move contents in content into root folder of new repo
3. git add commit push both repos
4. in root of site repo run following
  - git submodule add -b main git@github.com:QuintenMadari/yiqizuozuoye.git content
  - make sure the content folder has been removed, otherwise it will complain
5. profit! git add . commit push the site repo too
6. hugo -t book, to compile the public files again and host those each time. put the pulling and compiling into a cron

By turning the content folders (containing zh and py in this case) into a submodule, the site code separates from markdown posts.
I can now share the posts repo with a friend for collaboration.
 
