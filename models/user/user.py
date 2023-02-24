from dataclasses import dataclass

"""
Email用の値オブジェクト

― メールアカウント名とドメイン名を組み合わせた値
― メールアカウントとドメイン名前後の間に"@"を必ず含む必要がある
"""

@dataclass
class MailAddress:
    _mail_address: str

    @property
    def mail_address(self):
        if not "@" in self._mail_address:
            raise ValueError('メールアドレスには必ず"@"をつける必要があります')

        return self._mail_address



