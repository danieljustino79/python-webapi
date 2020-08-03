class User:
    users = {}

    def _contain_id(self, id_):
        return id_ in self.users

    def _next_id(self):
        self.users = self.get_users()
        _lenght = len(self.users)
        if _lenght == 0:
            return 1
        else:
            return _lenght + 1

    def add(self, name, email):
        if (len(name) < 2) or (len(email) < 3):
            return None
        else:
            next_id = self._next_id()
            _user = {
                'id': next_id,
                'name': name,
                'email': email
            }
            self.users[next_id] = _user
            return next_id

    def add_permission(self, id_, permissions):
        _list = list(permissions)
        if isinstance(id_, int) and self._contain_id(id_) and isinstance(_list, list):
            self.users[id_]['permissions'] = _list
            return id_
        else:
            return None

    def get_by_id(self, id_):
        if isinstance(id_, int) and self._contain_id(id_):
            return self.users[id_]
        else:
            return {}

    def get_users(self):
        return self.users
