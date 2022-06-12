# LibrarySDD

## Set-up database
1. Enter postgres console
   ```
   sudo -u postgres psql
   ```
2. Create database
   ```
   CREATE DATABASE <your_database_name>;
   ```
## Set-up project
1. Install `python3.8`
2. Clone repository
   ```
   git clone https://github.com/Ari100telll/LibrarySDD.git
   ```
3. From folder with project run
   ```
   cd ./LibrarySDD
   ```
4. Create _`.env`_ file
   ```
   nano .env
   ```
5. Copy the code with the replacement of variables with your own.
    ```
    DATABASE_URL=postgres://
    DB_NAME=<your_database_name>
    DB_USER=<your_database_user>
    DB_PASSWORD=<your_database_password>
    DB_HOST=127.0.0.1
    DB_PORT=5432
    ```

## Run project
1. Enter to the venv _(`. LibrarySDD/venv/bin/activate`)_
2. Install requirements `pip install -r requirements.txt`
3. Run `pre-commit install`
4. Run `python main.py`.

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

All endpoints should be added as flask blueprints and registered in the `main.py`

```python
test_bp = Blueprint('test_blueprint', __name__, url_prefix="/test")


@test_bp.route("/", methods=['GET', 'POST'])
def test():
    pass
```

```python
app.register_blueprint(test_bp)
```

<br>
<br>
<br>

#### Created by _IoT Students_
