# region pseudo_terminal definition
from r import make_pseudo_terminal
def pseudo_terminal(*_):pass # Easiest way to let PyCharm know that this is a valid def. The next line redefines it.
exec(make_pseudo_terminal)
# endregion
