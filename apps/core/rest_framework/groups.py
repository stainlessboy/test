def get_groups(user_type: str):
    from main.models import User
    from django.contrib.auth.models import Group
    group_names = {
        User.CLIENT: [ 'File manipulation'],
        User.ADMIN: [],
    }[user_type]  # TODO: add group names, statically or dynamically
    return Group.objects.filter(name__in=group_names)


def create_groups():
    groups = [

        dict(name='File manipulation', permissions_code_name=[
            'add_file',
            'change_file',
            'delete_file',
        ]),
        dict(name='File adding', permissions_code_name=[
            'add_file',
        ]),

    ]

    from django.contrib.auth.models import Permission, Group
    for group in groups:
        permissions = Permission.objects.filter(
            codename__in=group['permissions_code_name'])
        group, created = Group.objects.get_or_create(name=group['name'])
        group.permissions.set(permissions)


def set_groups_to_users(user_types=None):
    from main.models import User
    if not user_types:
        user_types = [User.ADMIN, User.CLIENT]
    users = list(User.objects.filter(user_type__in=user_types))
    for user in users:
        user.groups.set(get_groups(user.user_type))
