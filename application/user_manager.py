class UserManager:
    users = {}

    @staticmethod
    def _contains_id(_id):
        return _id in UserManager.users

    @staticmethod
    def _next_id():
        lenght = len(UserManager.users)
        if lenght == 0:
            return 1
        else:
            return lenght + 1

    @staticmethod
    def add(name, email):
        if (len(name) < 2) or (len(email) < 3):
            return None
        else:
            next_id = UserManager._next_id()
            user = {
                'id': next_id,
                'name': name,
                'email': email,
                'permissions': []
            }
            UserManager.users[next_id] = user
            return next_id

    @staticmethod
    def add_permission(_id, permission):
        try:
            _list = list(permission)
            if type(_id) is int and UserManager._contains_id(_id):
                UserManager.users[_id]['permissions'] = _list
                return True
            else:
                return False
        except TypeError:
            return False

    @staticmethod
    def get_by_id(_id):
        if type(_id) is int and UserManager._contains_id(_id):
            return UserManager.users[_id]
        else:
            return None

    @staticmethod
    def get_users():
        _users = []
        for key, value in UserManager.users.items():
            _users.append(value)

        return _users
