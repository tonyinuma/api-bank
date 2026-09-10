from app.schemas.account import (
    AccountCreate,
    AccountStatus,
)
from decimal import Decimal

class AccountRepository:
    def __init__(self) -> None:
        self._accounts: list[dict] = []
        self._current_id = 0

    async def find_all(self) -> list[dict]:
        return self._accounts

    async def find_by_id(
        self,
        account_id: int,
    ) -> dict | None:
        return next(
            (
                account
                for account in self._accounts
                if account["id"] == account_id
            ),
            None,
        )

    async def create(
        self,
        data: AccountCreate,
    ) -> dict:
        self._current_id += 1

        account = {
            "id": self._current_id,
            "customer_name": data.customer_name,
            "currency": data.currency,
            "status": AccountStatus.ACTIVE,
            "balance": Decimal("0.0"),
        }

        self._accounts.append(account)

        return account

    async def update_balance(
        self,
        account_id: int,
        new_balance: Decimal,
    ) -> dict | None:
        account = await self.find_by_id(account_id)

        if account is None:
            return None

        account["balance"] = new_balance

        return account