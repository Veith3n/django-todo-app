#  Sample django todo app
Simple django web application with basic auth to manage your Todos.

## Project setup

### Requirements
##### For running the app
- Installed `docker compose`.
- Windows users must install `jq` additionally.

##### For developing the app
- Installed `pipenv` (for adding new dependencies).

#### Running the app
3. Run `$ cp .env.sample .env.dev` and fill in the envs
3. Run `$ cp .env.sample.postgres .env.postgres` and fill in the envs
2. Run the app with `$ ./run_app`
3. Go to the `localhost:8000`

### Development
1. Install new dependencies with `$ pipenv install package_name`.
