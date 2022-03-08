import click

from ..version import __version__


def create_dagster_ml_cli():
    commands = {}

    @click.group(
        commands=commands,
        context_settings={"max_content_width": 120, "help_option_names": ["-h", "--help"]},
    )
    @click.version_option(__version__, "--version", "-v")
    def group():
        "CLI tools for working with dagster-ml."

    return group


ENV_PREFIX = "DAGSTER_ML_CLI"
cli = create_dagster_ml_cli()


def main():
    cli(auto_envvar_prefix=ENV_PREFIX)  # pylint:disable=E1123
