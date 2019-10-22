## Installation

Run the [pip](https://pip.pypa.io/en/stable/) command to install the latest version:

```bash
   pip install git+https://github.com/sitmena/numberToWords.git@v1.0
```

## Usage

```python
from number_to_words import number_to_words

number_to_words(323424.2)
'ثلاثمائة و ثلاثة و عشرون ألفاً و أربعمائة و أربعة و عشرون , عشرون

number_to_words(323424.2, to='currency', currency='SR') #Avilabel currencies: 'SAR', 'EUR', 'USD', 'EGP' and 'KWD'
#'ثلاثمائة و ثلاثة و عشرون ألفاً و أربعمائة و أربعة و عشرون ريالاً و عشرون هللة'

```
