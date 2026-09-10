from app.repositories.account_repository import (
    AccountRepository,
)
from app.services.account_service import AccountService


_repository = AccountRepository()


def get_account_service() -> AccountService:
    return AccountService(
        repository=_repository
    )