import os
import subprocess
import sys


def is_39():
    return sys.version_info >= (3, 9)


def main(quiet):
    """
    Python 3.9 Notes
    ================
    Especially on macOS, there are still many missing wheels for Python 3.9, which means that some
    dependencies may have to be built from source. You may find yourself needing to install system
    packages such as freetype, gfortran, etc.; on macOS, Homebrew should suffice.
    """

    # Previously, we did a pip install --upgrade pip here. We have removed that and instead
    # depend on the user to ensure an up-to-date pip is installed and available. If you run into
    # build errors, try this first. For context, there is a lengthy discussion here:
    # https://github.com/pypa/pip/issues/5599

    # On machines with less memory, pyspark install will fail... see:
    # https://stackoverflow.com/a/31526029/11295366
    cmd = ["pip", "--no-cache-dir", "install", "pyspark>=3.0.1"]
    if quiet:
        cmd.append(quiet)

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(" ".join(cmd))  # pylint: disable=print-call
    while True:
        output = p.stdout.readline()
        if p.poll() is not None:
            break
        if output:
            print(output.decode("utf-8").strip())  # pylint: disable=print-call

    install_targets = []

    # Need to do this for 3.9 compat
    # This is to ensure we can build Pandas on 3.9
    # See: https://github.com/numpy/numpy/issues/17784,
    if is_39():
        install_targets += ["Cython==0.29.21", "numpy==1.18.5"]

    install_targets += [
        "-e python_modules/dagster-ml[black,isort,mypy,test]",
    ]

    # NOTE: These need to be installed as one long pip install command, otherwise pip will install
    # conflicting dependencies, which will break pip freeze snapshot creation during the integration
    # image build!
    cmd = ["pip", "install"] + install_targets

    if quiet:
        cmd.append(quiet)

    p = subprocess.Popen(
        " ".join(cmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True
    )
    print(" ".join(cmd))  # pylint: disable=print-call
    while True:
        output = p.stdout.readline()
        if p.poll() is not None:
            break
        if output:
            print(output.decode("utf-8").strip())  # pylint: disable=print-call


if __name__ == "__main__":
    main(quiet=sys.argv[1] if len(sys.argv) > 1 else "")
