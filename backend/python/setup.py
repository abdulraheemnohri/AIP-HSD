from setuptools import setup, find_packages

setup(
    name="aiphsd-python",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi", "uvicorn", "pydantic", "sqlalchemy", "python-jose", "passlib"
    ],
)
