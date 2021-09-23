# Quick blog with hugo & github pages using submodule

## Courtesy of thesimpleengineer@youtube

1. Install hugo (on termux in my cade)
2. create 2 repos, 1 for code, 1 for deployment on github.io
 - 1st namenameblog, 2nd namename.github.io
3. while on github, navigate to gh-pages settings for io repo (append /settings to url)
4. go to https://themes.gohugo.io/ and select a theme. each theme works a bit different
5. in io repo, checkout -b main, touch readme.md, git add .; git commit -m "added readme"
  git push origin main
6. in code repo, hugo new site, apply theme submodule
  - in my case 
    git submodule add https://github.com/alex-shpak/hugo-book themes/book
7. in root folder nano config.toml change title, url and add theme = "THEMENAME"
8. exit, check if it runs locally by running hugo server (localhost:13130
  - it does! not on duckduckgobrowser tho, doesn't accept localhost
9. in root folder of code repo, git submodule add -b main [url] public
  - git submodule add -b main git@github.com:QuintenMadari/cc201zuoye.github.io.git public
10. In code repo, hugo new posts/test.md creates content/posts/test.md, I think manually is fine too
11. check appearance of post with hugo server localhost:1313
  - didn't work for book theme
  > By default, the theme will render pages from the content/docs section as a menu in a tree structure.
  > You can set title and weight in the front matter of pages to adjust the order and titles in the menu
12. create content/docs and put files in there
13. add example book config to config.toml, edit as desired
14. bit of a hassle to figure out how pahe order and weights work
15. root folder code repo, hugo -t theme, to create static files in public
  - hugo -t book
16. navigate to public, git add commit push
17. in io repo settings pages on gh, set the main branch to be hosted
18. turns out thesimpleengineer has something I dont. you can only publish to quintenmadari.github.io/name

