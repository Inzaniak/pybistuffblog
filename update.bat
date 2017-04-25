cd C:\Users\Inzaniak\Documents\new_site
nikola build
git remote add origin https://github.com/Inzaniak/pybistuffblog.git
git checkout -b gh-pages
git rm -rf
git commit -am "Update"
git push origin gh-pages
git checkout master
git branch -D gh-pages
git subtree split --prefix output -b gh-pages
git push -f origin gh-pages:gh-pages
git branch -D gh-pages