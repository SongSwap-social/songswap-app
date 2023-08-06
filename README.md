
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>songswap-app
</h1>
<h3>Developed with the software and tools listed below</h3>

<p align="center">
<img src="https://img.shields.io/badge/Docker-3.8-2496ED.svg?style&logo=Docker&logoColor=2496ED" alt="Docker" />
<img src="https://img.shields.io/badge/Python-3.10.12-3776AB.svg?style&logo=Python&logoColor=3776AB" alt="Python" />
<img src="https://img.shields.io/badge/Flask-2.3.2-000000.svg?style&logo=Flask&logoColor=white" alt="Flask" />
<br>
<img src="https://img.shields.io/badge/PostgreSQL-4169E1.svg?style&logo=postgresql&logoColor=white" alt="postgresql" />
<a href="https://github.com/spotipy-dev/spotipy"><img src="https://img.shields.io/badge/Spotipy-2.23.0-1DB954.svg?style&logo=spotify&logoColor=1DB954" alt="Spotipy" /></a>
<br>
<a href="https://github.com/apache/echarts"><img src="https://img.shields.io/badge/Apache_ECharts-5.4.2-AA344D.svg?style&logo=apacheecharts&logoColor=AA344D" alt="apacheecharts" /></a>
<a href="https://github.com/jgthms/bulma"><img src="https://img.shields.io/badge/Bulma-0.9.4-00D1B2.svg?style&logo=bulma&logoColor=00D1B2" alt="bulma" /></a>
<img src="https://img.shields.io/badge/FontAwesome-4.7.0-528DD7.svg?style&logo=fontawesome&logoColor=528DD7" />
<br>
<img src="https://img.shields.io/badge/Amazon RDS-527FFF.svg?style&logo=amazonrds&logoColor=white" alt="Amazon RDS" />
<img src="https://img.shields.io/badge/Amazon S3-569A31.svg?style&logo=amazons3&logoColor=white" alt="Amazon S3" />
<img src="https://img.shields.io/badge/Amazon EC2-FF9900.svg?style&logo=amazonec2&logoColor=white" alt="Amazon EC2" />
<img src="https://img.shields.io/badge/Amazon CloudWatch-FF4F8B.svg?style&logo=amazoncloudwatch&logoColor=white" alt="Amazon CloudWatch" />
</p>
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)

---


## 📍 Overview

This repository is a Flask web application that provides users with the ability to register using their Spotify account, access their listening history, and view insights into their top tracks, artists, and genres.

Every hour, the user's listening history data is retrieved from Spotify from the [songswap-airflow](https://github.com/SongSwap-social/songswap-airflow) project and stored in an AWS-backed PostgreSQL database. Insights are acquired from the [songswap-insights](https://github.com/SongSwap-social/songswap-insights) API.

The project's core functionalities include:
- user registration using OAuth authentication with Spotify
- periodic retrieving, storing and transforming user listening history
- interactive charts and graphs for personalized insights per track, artist, user, or time period (last week/month/etc.)

This application aims to enhance the user's music discovery experience by analyzing their listening patterns and providing tailored insights. In the future, the project will allow users to create user groups and share their insights with other users, or even discover other users with similar listening patterns.

The goal is to intertwine Spotify Wrapped and Myspace to provide an experience for music discovery, where users can share their music tastes and discover new music through their friends.

---

## ⚙️ Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The codebase follows a typical Flask application architecture, with separate blueprints for different functionalities. It uses `SQLAlchemy` for database operations and `Alembic` for database migrations. The application can be deployed in a container using Docker.    |
| **📖 Documentation**   | The codebase includes inline code comments in most files, providing explanations and details about the code. Some files have additional README files explaining their purpose and usage. However, more comprehensive documentation, like a detailed architectural overview or API documentation, could be beneficial.    |
| **🔗 Dependencies**    | The codebase has dependencies on Flask, SQLAlchemy, Alembic, spotipy, Pyecharts, and authlib libraries. `Flask` and `SQLAlchemy` handle the core components of the web application and database operations. `Alembic` is used for database migrations, `spotipy` for Spotify authentication, `Pyecharts` for visualizations, and `authlib` for OAuth integration.    |
| **🧩 Modularity**      | The codebase is modular, with separate blueprints for different functionalities like authentication, insights, health checks, and history. Models, forms, routes, and helper functions are segregated into their respective blueprints, making the codebase more maintainable and extensible.    |
| **✔️ Testing**          | The codebase does not have front-end tests at the moment. The majority of the testing codebase focuses on testing the backend API and Airflow orchestration workflows.    |
| **⚡️ Performance**      | The code's performance benefits from the performance capabilities of the underlying WSGI server (Gunicorn) and Flask's lightweight nature. Performance improvements are achieved by caching strategies, optimizing database queries, and implementing load balancing techniques (on AWS's ElasticBeanstalk) for increased scalability.    |
| **🔐 Security**        | The codebase incorporates the authentication mechanism using OAuth integration with Spotify's API, ensuring secure and authorized access to user data. Moreover, Alembic is used for database migrations, which assists in maintaining the integrity and security of the application's database schema and data.    |
| **🔌 Integrations**    | The codebase integrates with various external systems and services. It uses songswap-insights for user-specific insights data, authlib for OAuth integration with Spotify API, spotipy library for handling Spotify authentication flow, and Pyecharts for data visualization. These integrations enable seamless interaction with third-party systems and enrich the functionality.

---


## 📂 Project Structure


```bash
repo
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   ├── blueprints
│   │   ├── __init__.py
│   │   ├── auth
│   │   │   ├── __init__.py
│   │   │   ├── forms.py
│   │   │   ├── models.py
│   │   │   ├── providers.py
│   │   │   └── routes.py
│   │   ├── health
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── history
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   └── routes.py
│   │   └── insights
│   │       ├── __init__.py
│   │       ├── forms.py
│   │       ├── helpers.py
│   │       └── routes.py
│   ├── database.py
│   ├── static
│   │   └── styles.css
│   └── templates
│       ├── auth_home.html
│       ├── base.html
│       ├── insights.html
│       ├── insights_global.html
│       ├── navbar.html
│       ├── register.html
│       └── unauth_home.html
├── buildspec.yml
├── config.py
├── entrypoint.sh
├── migrations
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── 35e0533671ef_create_trackpreviews_table.py
│       ├── 36d8ca5b553b_standardize_table_names_to_pascalcase_.py
│       ├── 4ba4facc166c_initial_db_migration.py
│       ├── 86cecbe1fd2b_create_new_image_popularity_genre_.py
│       ├── bdd4bb2eaf3c_add_history_track_artist_tables.py
│       ├── e381845baba9_remove_redundant_spotify_id.py
│       └── manual_add_cascade_delete_update.py
├── render.html
├── requirements.txt
├── run.py
└── scripts
    ├── flush_db.sh
    └── init_db.sh

11 directories, 46 files
```

---

## 🧩 Modules

<details closed><summary>Root</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                  |
| ---           | ---                                                                                                                                                                                                                                                                                                                      |
| run.py        | Initializes a Flask application using the "create_app" function from the "app" module. It then starts the application using the "run" method with the value of the "DEBUG" configuration as the debug mode.                                                                                             |
| config.py     | Loads environment variables, such as DEBUG, SECRET_KEY, and database connection URI, from a `.env` file. It also sets the API URL based on whether the application is running locally or in a Docker container.                                                                                           |
| Dockerfile    | This Dockerfile sets up a Python Flask application in a container. It installs dependencies, sets environment variables, performs database migrations, and runs the app using Gunicorn on port 80.                                                                                                                       |
| entrypoint.sh | Upgrades, or initializes, the database using `flask db upgrade` and then executes the provided command.                                                                                                                                                                                                                   |

</details>

<details closed><summary>Migrations</summary>

| File           | Summary                                                                                                                                                                                                                                                                                                                                                                                            |
| ---            | ---                                                                                                                                                                                                                                                                                                                                                                                                |
| script.py.mako | Template for database migrations with `Alembic`. It generates a revision ID along with any revisions and dependencies. The code includes an `upgrade()` function for applying changes and a `downgrade()` function for reverting changes. The imports and revisions are parameterized for customization. It's a flexible and maintainable approach to managing database schema updates. |
| env.py         | This code snippet provides functionalities for running migrations using Alembic in a Flask application. It includes methods for running migrations offline and online, configuring the context, logging, and obtaining the engine URL.                                                                                                                                                             |
| README.md      | This code snippet provides minimal information about the database migrations, such as how they are performed.                                                                                                                                                                                                                                                                                                                               |

</details>

<details closed><summary>App</summary>

| File        | Summary                                                                                                      |
| ---         | ---                                                                                                          |
| database.py | The code snippet initializes a SQLAlchemy object called `db` for database operations in a Flask application. |

</details>

<details closed><summary>Insights</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| helpers.py | Provides helper functions for retrieving and formatting data from the `songswap-insights` API. Functions are included to retrieve the top tracks, top artists, and top genres from the API. The functions execute GET requests to the API, handle the response, and return the requested data.                                                                                                                                                                                                                     |
| routes.py  | Two routes: "/insights" and "/insights_global". The "/insights" route retrieves the user's top tracks from the `songswap-insights` API, converts the track duration to minutes and seconds, and renders the data using the "insights.html" template. The "/insights_global" route retrieves various statistics from the songswap-insights API, including total and distinct listens, total listen time, top tracks, and top artists. This data is then rendered using the "insights_global.html" template. |

</details>

<details closed><summary>Auth</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| models.py    | Defines two database models: "Users" and "SpotifyTokens". Users model has columns for user details, a relationship with SpotifyTokens, and a relationship with History. SpotifyTokens model has columns for access and refresh tokens. The code also includes methods for `Flask-Login` integration and administrative interface. Overall, the code sets up the database schema for storing user and Spotify token information. |
| forms.py     | This code snippet defines a `FlaskForm` called `RegistrationForm` for user registration. It includes fields for username and email, with validation for required input and unique username/email.                                                                                                                                                                                                                |
| providers.py | Defines an abstract class for a music authentication provider, and implements a concrete class for Spotify authentication. It integrates with the `spotipy` library to handle Spotify authentication flow and provides methods for obtaining authorization URL, access token and user information.                                                                                                                                      |
| routes.py    | This code snippet includes Flask routes and functions for Spotify OAuth authentication, user registration, and user login/logout functionalities for a web application. It uses the `authlib` library for OAuth integration and interacts with the Spotify API to obtain user information and access tokens. The code handles user creation if they don't exist and provides routes for authenticated and unauthorized users.                     |

</details>

<details closed><summary>Health</summary>

| File      | Summary                                                                                                                                                                                                                 |
| ---       | ---                                                                                                                                                                                                                     |
| routes.py | The provided code creates a route "/health" in a Flask Blueprint that performs a health check on the app, checking its critical functions. It returns a 200 status code and "OK" if everything is functioning properly. |

</details>

<details closed><summary>History</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---       | ---                                                                                                                                                                                                                                                                                                                                                                                                                     |
| models.py | This code snippet defines a set of `SQLAlchemy` models that represent different entities in a database. These entities include history, artists, tracks, artist tracks, track popularity, track features, track images, track previews, artist images, artist popularity, artist genres, and artist followers. The relationships between these entities are defined using foreign key constraints and cascading behavior. |
| routes.py | This code snippet defines a Flask blueprint for handling user history. The `/history` route requires authentication, and when accessed, it returns the user's listening history.                                                                                                                                                                                                                                         |

</details>

<details closed><summary>Templates</summary>

| File                 | Summary                                                                                                                                                                                                                                                                                                                                                |
| ---                  | ---                                                                                                                                                                                                                                                                                                                                                    |
| navbar.html          | This code snippet represents a navigation bar in HTML that allows users to navigate through different sections of a website. It includes features like displaying user-specific options, such as groups and insights, when a user is logged in. It also provides options for users to view their profile, account settings, report bugs, and sign out. |
| unauth_home.html     | The code snippet extends a base HTML template and defines a "content" block. It includes a title, description, and a button that enables a user to login with Spotify through a provided auth URL.                                                                                                                                                     |
| insights_global.html | The code snippet is a template for displaying insights about all users. It shows the total number of tracks listened to, unique tracks and artists, and total listen duration. It also displays tables for the top 10 artists and tracks based on counts. The template includes scripts for charting and table functionality.                          |
| base.html            | This code snippet is for the base template of a web application. It includes the necessary HTML, CSS, and JavaScript code to create a responsive layout, handle flash messages, and provide functionality for dismissing those messages.                                                                                                               |
| auth_home.html       | The provided code snippet extends a base HTML template and displays an authenticated homepage using the Bulma CSS framework. It features a hero section with centered text and a welcome message that includes the current user's username.                                                                                                            |
| register.html        | The provided code snippet extends a base HTML template and creates a register form. It includes fields for username and email, and a submit button. The form captures user input and can be processed through a POST method.                                                                                                                           |
| insights.html        | The provided code snippet is a template for an insights page. It displays a table of the top 10 tracks and their respective details such as rank, track name, artist name, duration, and play count. Each track has a play button that toggles play/pause of a track preview. It also includes a modal for additional content display.                 |

</details>

<details closed><summary>Scripts</summary>

| File        | Summary                                                                                                                                                                                                                                              |
| ---         | ---                                                                                                                                                                                                                                                  |
| init_db.sh  | The provided code snippet initializes a database for a Flask application by creating the necessary migrations. After initializing, it performs the initial migration with a commit message and finally upgrades the database to reflect the changes. |
| flush_db.sh | The provided code snippet clears the database file and removes all migration files for the application site.                                                                                                                                         |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ docker`
> - `ℹ️ songswap-insights`
> - `ℹ️ songswap-airflow`

### 📦 Installation

1. Clone the songswap-app repository:
```sh
git clone git@github.com:SongSwap-social/songswap-app.git
```

2. Change to the project directory:
```sh
cd songswap-app
```

3. If **running locally** and not in Docker, install the dependencies:
```sh
pip install -r requirements.txt
```

### 🎮 Using songswap-app

- Run the application locally, for testing or development purposes:
```sh
python main.py
```

- Run the application in a Docker container:
```sh
docker build -t songswap-app .
docker run songswap-app
```

---


## 🗺 Roadmap

> - [X] `ℹ️  Add Spotify OAuth authentication and user registration`
> - [X] `ℹ️  Generate charts and graphs for insights`
> - [X] `ℹ️  Migrate from local infra to hybrid AWS`
> - [ ] `ℹ️  Add user groups and sharing functionality`
> - [ ] `ℹ️  Add a search feature for users and groups`
> - [ ] `ℹ️  Create public user profiles with a feed of their insights`
> - [ ] `ℹ️  Allow users to post on their own and friends' profiles`
> - [ ] `ℹ️  Create a homepage with a feed of friends' insights and posts`
> - [ ] `ℹ️  Add a chat box feature`


---
