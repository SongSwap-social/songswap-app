Single-database configuration for Flask.

### Adding to the Database

When you make changes to your database models, you would:
    - Update your SQLAlchemy models in your Python code (typically a `models.py` file)
    - Run `flask db migrate -m "Insert message explaining changes"` locally to generate a new migration script.
    - Review the generated migration script in `migrations/versions/` directory. It's important to check the generated SQL and ensure it's doing what you expect, as automated migration has its limits.
    - Commit and push both your changes to the models and the new migration script. This will trigger a new build and deployment.
    - As part of the deployment, `flask db upgrade` will run and apply the migration script to your database, bringing it up to date with your models.

This process will work well for additive changes to your models (like adding a new table or a new column).
If you need to perform more complex migrations, you may need to edit the migration scripts manually, or perform some database operations manually.
