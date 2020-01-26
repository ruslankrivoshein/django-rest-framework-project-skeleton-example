# Skeleton for DRF-project with nginx, PostgreSQL and JSON:API in Docker

First, put your ssl-data to `./conf.d/nginx/ssl/..` or remove lines with `ssl` from `./conf.d/nginx/conf.d/app.conf`. Then you must create and fill `.env` file:
`cp .env.example .env`.

For more comfort create few aliases:  
`alias dc='docker-compose'`  
`alias mng='dc exec app ./manage.py'`  

So, now you can start your docker-stack, but firstly you must create volume for PostgreSQL:  
`docker volume create --name=main_postgres`  

After that execute `dc up -d --build` - your stack is up. And subsequent commands you should perform for containers.

For app you must run a batch of commands:  
`mng collectstatic` - places static files of packages to your `static` dir  
`mng migrate` - performs base django migrations  
`mng makemigrations ; mng migrate` - here perform migrations for your models  
`mng createsuperuser` - and create admin  

Example contains not so many tests, but all the same:  
`mng test`  

And keep in mind security!
