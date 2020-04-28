docker run --rm -it \
-p 5000:5000 \
-v `pwd`/app:/flasktasklist/app \
igormcsouza/python-webapps:flasktasklist