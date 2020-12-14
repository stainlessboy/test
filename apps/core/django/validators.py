from django.core.validators import RegexValidator

phone_validator = RegexValidator(r'^\+?\d{7,15}$', 'Only numbers and sign + allowed')
date_validator = RegexValidator(r'^(\d{4}-\d{2}-\d{2})|(present)$', 'Input is not date, or `present`')
size_expression_validator = RegexValidator(r'(^\<?\>?\=?\d{1,10}$)|(^\d{1,10}\<?\>?\=?$)|(^\d{1,10}-\d{1,10}$)',
                                           'Input may include characters such as >,<,=,- and numbers')
tags_validator = RegexValidator(r'^\w+(?:(,\s\w+)|)+$', 'Input should be like `hello, world, what`')
age_range_validator = RegexValidator(r'^(?!-)[0-9]{0,3}($|(?:-[0-9]{0,3}$))', 'Input can be as `10` or `10-20`')
service_code_validator = RegexValidator(r'^(ES|AS|DA|VP|FB)(\d+|(\d+_\d+))$',
                                        'Input should have one of prefixes ES, AS, DA, VP, FB and number as suffix')
