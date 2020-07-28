users = {}


def next_id():
    global users
    lenght = len(users)
    if lenght == 0:
        return str(1)
    else:
        return str(lenght + 1)


def contain_id(id):
    return str(id) in users


def add(name, email):
    global users
    nextId = next_id()
    users[nextId] = {
        'id': nextId,
        'name': name,
        'email': email
    }

    return True


def add_permission(id, permissions):
    global users
    if isinstance(id, int) and contain_id(id) and isinstance(permissions, list):
        users[str(id)]['permissions'] = list(permissions)
        return True
    else:
        return False


def get():
    return users


def get_by_id(id):
    global users
    if isinstance(id, int) and contain_id(id):
        index = str(id)
        return users[index]
    else:
        return {}


def remove(id):
    global users
    if str(id) in users:
        users.pop(id)
        return True

    return False

