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

Example output with --format gcc

-:230:7: warning: Quote this to prevent word splitting. [SC2046]
-:230:7: note: Useless echo? Instead of 'echo $(cmd)', just use 'cmd'. [SC2005]
-:230:158: note: Double quote to prevent globbing and word splitting. [SC2086]
-:234:10: error: Add double quotes around ${VAR[@]}, otherwise it's just like $* and breaks on spaces. [SC2068]
2.rc:1:1: note: This shebang was unrecognized. Note that ShellCheck only handles sh/bash/ksh. [SC1008]
2.rc:3:18: warning: This { is literal. Check expression (missing ;/\n?) or quote it. [SC1083]
2.rc:4:1: warning: To assign the output of a command, use var=$(cmd) . [SC2037]
2.rc:4:11: error: Don't put spaces around the = in assignments. [SC1068]
2.rc:4:13: note: Use $(..) instead of legacy `..`. [SC2006]
2.rc:4:15: error: You need a space after the '{'. [SC1054]
2.rc:4:34: warning: This } is literal. Check expression (missing ;/\n?) or quote it. [SC1083]
2.rc:5:6: warning: uhrzeit_0 is referenced but not assigned. [SC2154]
2.rc:5:6: note: Double quote to prevent globbing and word splitting. [SC2086]
2.rc:14:14: warning: This { is literal. Check expression (missing ;/\n?) or quote it. [SC1083]
2.rc:14:34: warning: This } is literal. Check expression (missing ;/\n?) or quote it. [SC1083]
v@v:~/rc$ rc -n
; exit
v@v:~/rc$ rc -n 2.rc 
v@v:~/rc$ rc -n 2.rc 
v@v:~/rc$ rc -n 2.rc 
v@v:~/rc$ rc -n 2.rc 
rc: line 9: syntax error near '='


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
