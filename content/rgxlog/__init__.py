from typing import Any

import sys
sys.path.append('/drive/spanner_workbench/src/rgxlog_interpreter/src/')
sys.path.append('/drive/spanner_workbench/src/rgxlog_interpreter/src/rgxlog/')

import rgxlog.engine
import rgxlog.grammar
from spanner_workbench.src.rgxlog_interpreter.src.rgxlog.engine.session import *
from rgxlog.magic.rgxlog_magic import RgxlogMagic
from IPython import InteractiveShell, get_ipython

magic_session = Session()


def load_ipython_extension(ipython: InteractiveShell) -> None:
    # this method gets called when running `%load_ext rgxlog` or `import rgxlog` in jupyter
    ipython.register_magics(RgxlogMagic)


try:
    load_ipython_extension(get_ipython())

except (AttributeError, ImportError):
    pass
