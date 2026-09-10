from fastapi import HTTPException, status

from app.repositories.account_repository import AccountRepository
from app.schemas.account import AccountCreate


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