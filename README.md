# LibrarySDD

## Set-up project

1. _`.env`_ file should be on `LibrarySDD/` level.
2. _`.env`_ structure:
    ```
    DATABASE_URL=postgres://
    DB_NAME=db_name
    DB_USER=db_user
    DB_PASSWORD=db_password
    DB_HOST=127.0.0.1
    DB_PORT=5432
    ```

## Run project

1. Enter to the venv _(`. LibrarySDD/venv/bin/activate`)_
2. Install requirements `pip install -r requirements.txt`
3. Run `pre-commit install`
4. Run `main.py` file.

## Structure

### Models

Models should be in directory `models`

### Controllers

Controllers should be in directory `controllers`

### Services

Services should be in directory `services`

### Utils

All helpers should be in directory `utils`
### Config

All configurations should be in directory `config`

## Add endpoint

All endpoints should be added in file `urls.py` using `UrlManager`
```url_manager.add_endpoint('/ping', 'ping', ping, methods=['GET'])```

<br>
<br>
<br>

#### Created by _IoT Students_
