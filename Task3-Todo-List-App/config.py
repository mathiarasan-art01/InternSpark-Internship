import os


BASE_DIR = os.path.abspath(
    os.path.dirname(__file__)
)


class Config:
    """
    TaskNest Application Configuration
    """

    # ==================================================
    # Security
    # ==================================================
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "dev-tasknest-secret-change-me"
    )

    # ==================================================
    # Base Directory
    # ==================================================
    BASE_DIR = BASE_DIR

    # ==================================================
    # Database
    # ==================================================
    DATABASE_DIR = os.path.join(
        BASE_DIR,
        "database"
    )

    DATABASE_PATH = os.path.join(
        DATABASE_DIR,
        "tasknest.db"
    )

    SCHEMA_PATH = os.path.join(
        DATABASE_DIR,
        "schema.sql"
    )

    # ==================================================
    # Exports
    # ==================================================
    EXPORT_DIR = os.path.join(
        BASE_DIR,
        "exports"
    )

    REPORT_DIR = os.path.join(
        EXPORT_DIR,
        "reports"
    )

    # ==================================================
    # Logging
    # ==================================================
    LOG_DIR = os.path.join(
        BASE_DIR,
        "logs"
    )

    # ==================================================
    # Application Constants
    # ==================================================
    PRIORITIES = (
        "Low",
        "Medium",
        "High"
    )

    CATEGORIES = (
        "General",
        "Work",
        "Study",
        "Personal",
        "Ideas",
        "Health"
    )

    JSON_SORT_KEYS = False

    # ==================================================
    # Bootstrap Settings
    # ==================================================
    BOOTSTRAP_SERVE_LOCAL = True

    # ==================================================
    # Create Required Directories
    # ==================================================
    os.makedirs(DATABASE_DIR, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(EXPORT_DIR, exist_ok=True)
    os.makedirs(REPORT_DIR, exist_ok=True)