from datetime import date


def completed_percentage(obj, fields: dict):
    per_percentage = 100 / len(fields)
    total = 0
    for k, v in fields.items():
        if isinstance(v, bool) and bool(getattr(obj, k, False)) is True:
            total += per_percentage
        elif isinstance(v, int):
            value = getattr(obj, k, None)
            if value.__class__.__name__ == 'ManyRelatedManager' and getattr(value, 'count')() > v:
                total += per_percentage
            elif isinstance(value, list) and len(value) > v:
                total += per_percentage
        elif isinstance(v, list):
            max_filled = 0
            len_required_fields = len(v)
            if 'group_' not in k:
                model_field = getattr(obj, k, None)
                if model_field:
                    if model_field.__class__.__name__ == 'ManyRelatedManager':
                        related_objs = list(model_field.all())
                        for related_obj in related_objs:
                            sub_max_filled = 0
                            for sub_field in v:
                                if bool(getattr(related_obj, sub_field, None)):
                                    sub_max_filled += 1
                            if sub_max_filled > max_filled:
                                max_filled = sub_max_filled
            else:
                for field in v:
                    if bool(getattr(obj, field, None)):
                        max_filled += 1
            total += (max_filled / len_required_fields) * per_percentage

    return total


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age
