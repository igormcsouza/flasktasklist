# Flask Tasklist

Simple tasklist made with [Flask framework](https://flask.palletsprojects.com/en/1.1.x/) from python.

## Fire up the app on localhost

The application was built to work on development too, that means you will need to set the environment variables, such as:

    POSTGRES_USER=db
    POSTGRES_PASSWORD=pwd
    POSTGRES_TYPE=db
    POSTGRES_PORT=5432
    POSTGRES_DB=db
    APP_SECRET_KEY=flasktaskapp
    PYTHONUNBUFFERED=true

After that, you must fire the the application using docker-compose (use the `--build` )

    docker-compose up -d --build

Stop the application using

    docker-compose stop

## How to start DB

Enter python shell and execute the following code (on heroku you may need enter `app` folder first)

    from app import create_db
    create_db()