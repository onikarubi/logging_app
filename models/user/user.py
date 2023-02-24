from dataclasses import dataclass

"""
ユーザー名の規約を定義する値オブジェクト

- ユーザー名はフルネーム形式で入力する必要がある
- 空文字は排除
"""


@dataclass
class UserName:
    first_name: str
    last_name: str

    def __post_init__(self):
        if not self.first_name or not self.last_name:
            raise ValueError('空白または正しい文字が入力されていません')

        self.full_name = f"{self.first_name} {self.last_name}"


"""
Email用の値オブジェクト

― メールアカウント名とドメイン名を組み合わせた値
― メールアカウントとドメイン名前後の間に"@"を必ず含む必要がある
"""

@dataclass
class MailAddress:
    address: str

    def __post_init__(self):
        if not "@" in self.address:
            raise ValueError('メールアドレスには必ず"@"をつける必要があります')

    @property
    def mail_address(self):
        return self.address

"""
User用のエンティティを定義

- ユーザー用のデータを定義する
- ユーザーIDによる重複しないようにバリデーションをかける
"""
@dataclass
class User:
    id: int
    username: UserName
    email: MailAddress

    def change_username(self, username: UserName):
        self.username = username

    def change_email(self, email: MailAddress):
        self.email = email




