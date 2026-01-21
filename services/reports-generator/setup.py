from setuptools import find_packages, setup

setup(
    name="gp2gp-reports-generator",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "python-dateutil>=2.8",
        "boto3>=1.18",
        "urllib3==2.6.3",
        "PyArrow==23.0.0",
        "polars~=0.20.31",
    ],
)
