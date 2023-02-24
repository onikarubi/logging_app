from dataclasses import dataclass

"""
Email用の値オブジェクト

― メールアカウント名とドメイン名を組み合わせた値
― メールアカウントとドメイン名前後の間に"@"を必ず含む必要がある
"""


@dataclass
class MailAddress(object):
    address: str
    domain: str
    mail_address: str = f'{address}@{domain}'

    @property
    def mail_address(self):
        return self.mail_address


