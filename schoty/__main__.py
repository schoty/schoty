import os
import sys
import time
import argparse
from subprocess import call
from ._version import __version__

from .base import GitMonoRepo


def _clone(args):

    mr = GitMonoRepo.clone(args.repo, args.dir, shallow=True)


def _info(args):
    print(f'Schoty - version {__version__}')


# Allow to propagate formatter_class to subparsers
# https://bugs.python.org/issue21633

class _ArgParser(argparse.ArgumentParser):

    def __init__(self, **kwargs):
        kwargs["formatter_class"] = argparse.ArgumentDefaultsHelpFormatter
        super(_ArgParser, self).__init__(**kwargs)


def main(args=None, return_parser=False):
    """The main CLI interface."""

    parser = _ArgParser()
    subparsers = parser.add_subparsers(help='action')

    run_parser = subparsers.add_parser("clone",
                                       description='Create a new monorepo '
                                                   'from exising '
                                                   'repositories.')
    run_parser.set_defaults(func=_clone)

    # clone parser
    run_parser.add_argument('repo', nargs='+',
                            help='Path to the repositories')

    run_parser.add_argument('dir',
                            help='The output monorepo directory')

    info_parser = subparsers.add_parser("info",
                                        description='Show information on the '
                                                    'currrent monorepo')
    info_parser.set_defaults(func=_info)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
