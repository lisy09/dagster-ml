# Makefile oddities:
# - Commands must start with literal tab characters (\t), not spaces.
# - Multi-command rules (like `black` below) by default terminate as soon as a command has a non-0
#   exit status. Prefix the command with "-" to instruct make to continue to the next command
#   regardless of the preceding command's exit status.

pylint:
	pylint -j 0 `git ls-files '*.py'` --rcfile=.pylintrc

# NOTE: See pyproject.toml [tool.black] for majority of black config. Only include/exclude options
# and format targets should be specified here. Note there are separate pyproject.toml for the root
# and examples/docs_snippets.
#
# NOTE: Use `extend-exclude` instead of `exclude`. If `exclude` is provided, it stops black from
# reading gitignore. `extend-exclude` is layered on top of gitignore. See:
#   https://black.readthedocs.io/en/stable/usage_and_configuration/file_collection_and_discovery.html#gitignore
black:
	black --fast \
    --extend-exclude="examples/docs_snippets|snapshots" \
    examples python_modules

check_black:
	black --check --fast \
    --extend-exclude="examples/docs_snippets|snapshots" \
    examples python_modules

# NOTE: We use `git ls-files` instead of isort's built-in recursive discovery
# because it is much faster. Note that we also need to skip files with `git
# ls-files` (the `:!:` directives are exclued patterns). Even isort
# `--skip`/`--filter-files` is very slow.
isort:
	isort \
    `git ls-files 'examples/*.py' 'integration_tests/*.py' 'helm/*.py' 'python_modules/*.py' \
      ':!:examples/docs_snippets' \
      ':!:snapshots'`
	isort \
   `git ls-files 'examples/docs_snippets/*.py'`

check_isort:
	isort --check \
    `git ls-files 'examples/*.py' 'integration_tests/*.py' 'helm/*.py' 'python_modules/*.py' \
      ':!:examples/docs_snippets' \
      ':!:snapshots'`
	isort --check \
    `git ls-files 'examples/docs_snippets/*.py'`

yamllint:
	yamllint -c .yamllint.yaml --strict `git ls-files 'helm/**/*.yml' 'helm/**/*.yaml' ':!:helm/**/templates/*.yml' ':!:helm/**/templates/*.yaml'`

setup-dev-env:
	python  ${SCRIPT_DIR}/install_dev_python_modules.py -qqq

setup-dev-env-verbose:
	python  ${SCRIPT_DIR}/install_dev_python_modules.py