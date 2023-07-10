class User:
    def __init__(self, user, cookie=None):
        self.user = user
        self.cookie = cookie
        self.submissions = []
        self.problems = []

    def get_problems_solved(self):
        pass

    def get_submissions(self):
        pass

    def credentials(self):
        return {
            'user': self.user,
            'password': self.password,
            'cookie': self.cookie
        }

    def __str__(self):
        return f'User: {self.username}'
    