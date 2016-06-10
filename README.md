Prized.tv
========

## Setup

```
python manage.py collectstatic
python manage.py migrate
```

## Project structure

```
/fomotv - django project folder
    clientdev.py - app config for dev.prized.tv
    dev.py - app config for fomotv.websta.ru (old dev server). can be removed
    local.py - Nikolay's local config
    prod.py - prized.tv config
    settings.py - base config with common settings
    urls.py - app urls
    wsgi.py - WSGI config for fomotv project
/main
    /fixtures - fixtures for tests
    /migrations - db migrations
    /views - main app views
    pipeline.py - Hooks for saving additional info about users from social networks
    serializers.py - serializers for Django Rest Framework
    winner.py - script for determining the winners. run every day about 01:00 AM
/media - users files (avatars, photos etc)
/node_modules - js libs for grunt
/order - order app: working with paypal api, processing order, sending emails
/static
    /app - Angularjs application files. All files compile with gulp to dist/app.min.js
    /css - css files
    /dist - compiled js files
    /fonts - fonts
    /img - images
    /js - libs
    /slick - separate dir for gallery js lib
    /tests - test for js code
/templates
    /email - all email templates
    admin_filter.html - filter for product section in admin
    base.html - common template for all pages
install.txt - shell commands required for installation on new server
gulfile.js - gulp instructions
req.txt - python dependencies

```