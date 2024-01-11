# Sample django tasks app

Simple django web application with basic auth to manage your Tasks with simple activity log.

## Project setup

### Requirements

#### For running the app

- Installed `docker compose`.

#### For developing the app

- Installed `pipenv` (for adding new dependencies).

### Running the app

1. Run `$ cp .env.sample .env.dev` and fill in the envs
2. Run `$ cp .env.sample.postgres .env.postgres` and fill in the envs
3. Run the app with `$ docker compose up`
4. Seed the app with `$ ./seed_data`
5. Go to the `localhost:8000`
6. Credentials for the normal user: `login: nwright, password: 123QWE!@#` and admin: `login: root, password: admin`
7. Admin panel is accessible at `localhost:8000/admin`

### Development

1. Install new dependencies with `$ pipenv install package_name`.

### Functionalities

1. CRUD of users in the admin panel
2. Logging of the users to the app
3. CRUD of tasks per given user
4. Activity log tab for a given user (list of actions, done with tasks, sortable)
5. CRUD of tasks in the admin panel
6. Adding/modifying task's tags and displaying them, sort task by tags in the index view
