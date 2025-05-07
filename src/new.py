from pyobjus import autoclass
from pyobjus.dylib_manager import load_framework, INCLUDE


def localisation():
    load_framework(INCLUDE.Foundation)
    NSLocale = autoclass("NSLocale")
    current_locale = NSLocale.currentLocale
    return current_locale
