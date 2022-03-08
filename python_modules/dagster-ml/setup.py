from pathlib import Path
from typing import Dict

from setuptools import find_packages, setup  # type: ignore


def get_description() -> str:
    readme_path = Path(__file__).parent.parent.parent / "README.md"

    if not readme_path.exists():
        return """
        # Dagster

        The data orchestration platform built for productivity.
        """.strip()

    return readme_path.read_text()


def get_version() -> str:
    version: Dict[str, str] = {}
    with open("dagster_ml/version.py") as fp:
        exec(fp.read(), version)  # pylint: disable=W0122

    return version["__version__"]


if __name__ == "__main__":
    setup(
        name="dagster-ml",
        version=get_version(),
        author="lisy09",
        author_email="lisy09.thu@gmail.com",
        license="Apache-2.0",
        description="Dagster machine learning extension",
        long_description=get_description(),
        long_description_content_type="text/markdown",
        url="https://github.com/dagster-io/dagster",
        classifiers=[
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
        ],
        packages=find_packages(exclude=["dagster_ml_tests"]),
        package_data={"dagster-ml": []},
        include_package_data=True,
        install_requires=[
            "dagster~=0.14.3",
        ],
        extras_require={
            "docker": ["docker"],
            "test": [
                "astroid>=2.3.3,<2.5",
                "coverage==5.3",
                "docker",
                "freezegun>=0.3.15",
                "grpcio-tools==1.32.0",
                "mock==3.0.5",
                "objgraph",
                "protobuf==3.13.0",  # without this, pip will install the most up-to-date protobuf
                "pytest-cov==2.10.1",
                "pytest-dependency==0.5.1",
                "pytest-mock==3.3.1",
                "pytest-rerunfailures==10.0",
                "pytest-runner==5.2",
                "pytest-xdist==2.1.0",
                "pytest==6.1.1",
                "responses==0.10.*",
                "snapshottest==0.6.0",
                "tox==3.14.2",
                "tox-pip-version==0.0.7",
                "tqdm==4.48.0",  # pylint crash 48.1+
                "yamllint",
                "flake8>=3.7.8",
                "pylint==2.6.0",
            ],
            "black": [
                "black[jupyter]==22.1.0",
            ],
            "isort": [
                "isort==5.10.1",
            ],
            "mypy": [
                "mypy==0.931",
                "types-croniter",  # version will be resolved against croniter
                "types-mock",  # version will be resolved against mock
                "types-pkg-resources",  # version will be resolved against setuptools (contains pkg_resources)
                "types-python-dateutil",  # version will be resolved against python-dateutil
                "types-PyYAML",  # version will be resolved against PyYAML
                "types-pytz",  # version will be resolved against pytz
                "types-requests",  # version will be resolved against requests
                "types-tabulate",  # version will be resolved against tabulate
            ],
        },
        entry_points={
            "console_scripts": [
                "dagster-ml = dagster_ml.cli:main",
            ]
        },
    )
