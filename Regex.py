import re
import string

PATTERN_PHONENB = re.compile(
    r'(\(\+?0?84\))?(03|04|05|07|08|09|012|016|018|019)((\d(\s|\.|\,)*){8})',re.MULTILINE)

PATTERN_URL = re.compile(
        r'(((ftp|https?)\:\/\/)|(www\.))[\d\w\.\-\_]+\.[\w]{2,6}(:[\d\w]+)?[\#\d\w\-\.\_\?\,\'\/\\\+\;\%\=\~\$\&]*(.html?)?')

PATTERN_EMAIL = re.compile(
    r'(^|\W)([^@\s]+@[a-zA-Z0-9\-][a-zA-Z0-9\-\.]{0,254})(\W|$)')

PATTERN_NUMBER = re.compile(r'((\d+(\s|\.|\,|-){,2}\d*){1,})')

PATTERN_HTMLTAG = re.compile(r'<[^>]*>')

PATTERN_PUNCTATION = re.compile(r'([%s])' % re.escape(string.punctuation))

PATTERN_LINEBRK = re.compile(r'\t|\v|\f|(\s){2,}|\r\n|\r|\n')

PATTERN_NOT_PUNC_WSPACE_ALNUM = re.compile(r'[^%s\w\d]' % re.escape(
                    string.punctuation + string.whitespace), re.UNICODE)

PATTERN_FULLNAME = re.compile(r'([BCDĐGHKLMNPQRSTVXAÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶEÉÈẺẼẸÊẾỀỂỄỆIÍÌỈĨỊOÓÒỎÕỌƠỚỜỞỠỢÔỐỒỔỖỘUÚÙỦŨỤƯỨỪỬỮỰYÝỲỶỸỴ][bcdđghklmnpqrstvxaáàảãạâấầẩẫậăắằẳẵặeéèẻẽẹêếềểễệiíìỉĩịoóòỏõọơớờởỡợôốồổỗộuúùủũụưứừửữựyýỳỷỹỵ]+\s?){2,}', re.UNICODE)