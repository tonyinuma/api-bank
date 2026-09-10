from fastapi import APIRouter, Depends, status

from app.dependencies.accounts import get_account_service
from app.schemas.account import (
    AccountCreate,
    AccountResponse,
)
from app.services.account_service import AccountService


router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"],
)


@router.get(
    "",
    response_model=list[AccountResponse],
)
async def get_accounts(
    service: AccountService = Depends(
        get_account_service
    ),
):
    return await service.get_accounts()


@router.get(
    "/{account_id}",
    response_model=AccountResponse,
)
async def get_account(
    account_id: int,
    service: AccountService = Depends(
        get_account_service
    ),
):
    return await service.get_account(account_id)


@router.post(
    "",
    response_model=AccountResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_account(
    data: AccountCreate,
    service: AccountService = Depends(
        get_account_service
    ),
):
    return await service.create_account(data)