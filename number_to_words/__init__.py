from __future__ import unicode_literals
import re

from . import (lang_AR)

CONVERTER_CLASSES = {
    'ar': lang_AR.Num2Word_AR(),
}


CONVERTES_TYPES = ['cardinal', 'ordinal', 'ordinal_num', 'year', 'currency']


def number_to_words(number, ordinal=False, lang='en', to='cardinal', **kwargs):
    # We try the full language first
    if lang not in CONVERTER_CLASSES:
        # ... and then try only the first 2 letters
        lang = lang[:2]
    if lang not in CONVERTER_CLASSES:
        raise NotImplementedError()
    converter = CONVERTER_CLASSES[lang]

    if isinstance(number, str):
        number = converter.str_to_number(number)

    # backwards compatible
    if ordinal:
        return converter.to_ordinal(number)

    if to not in CONVERTES_TYPES:
        raise NotImplementedError()

    words =  getattr(converter, 'to_{}'.format(to))(number, **kwargs)
    return re.sub(' +', ' ', words)
