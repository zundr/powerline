# vim:fileencoding=utf-8:noet

from __future__ import absolute_import

import os
from powerline.bindings.vim import vim_getbufoption


def help(matcher_info):
	return str(vim_getbufoption(matcher_info, 'buftype')) == 'help'


def cmdwin(matcher_info):
	name = matcher_info['buffer'].name
	return name and os.path.basename(name) == '[Command Line]'


def quickfix(matcher_info):
	return str(vim_getbufoption(matcher_info, 'buftype')) == 'quickfix'
	#return str(getbufvar(matcher_info['bufnr'], '&buftype')) == 'quickfix'

def tagbar(matcher_info):
	name = matcher_info['buffer'].name
	return name and os.path.basename(name) == '__Tagbar__'

def unite(matcher_info):
	return str(vim_getbufoption(matcher_info, 'filetype')) == 'unite'
	#return str(getbufvar(matcher_info['bufnr'], '&filetype')) == 'unite'
