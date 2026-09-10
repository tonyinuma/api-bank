from fastapi import HTTPException, status

from app.repositories.account_repository import AccountRepository
from app.schemas.account import (
    AccountCreate,
    AccountStatus,
)
from decimal import Decimal

class AccountService:
    def __init__(
        self,
        repository: AccountRepository,
    ) -> None:
        self.repository = repository

    async def get_accounts(self) -> list[dict]:
        return await self.repository.find_all()

    async def get_account(
        self,
        account_id: int,
    ) -> dict:
        account = await self.repository.find_by_id(
            account_id
        )

        if account is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Account not found",
            )

        return account

    async def create_account(
        self,
        data: AccountCreate,
    ) -> dict:
        return await self.repository.create(data)

    async def deposit(
        self,
        account_id: int,
        amount: Decimal,
    ) -> dict:
        account = await self.repository.find_by_id(
            account_id
        )

        if account is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Account not found",
            )

        if account["status"] != AccountStatus.ACTIVE:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Account is not active",
            )

        new_balance = account["balance"] + amount

        return await self.repository.update_balance(
            account_id=account_id,
            new_balance=new_balance,
        )