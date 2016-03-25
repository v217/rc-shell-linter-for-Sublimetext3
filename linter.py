#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by NotSqrt
# Copyright (c) 2013 NotSqrt
#
# License: MIT
#

"""
This module exports the rc plugin class.
"""

from SublimeLinter.lint import Linter


class Shellcheck(Linter):

    """Provides an interface to shellcheck."""

    syntax = 'rc shell plan9'
    cmd = 'rc -n'
    regex = (
        r'^rc: line (?P<line>\d+):(?P<message>.+)$'
    )

    defaults = {
        '--exclude=,': ''
    }
    inline_overrides = 'exclude'
    comment_re = r'\s*#'
