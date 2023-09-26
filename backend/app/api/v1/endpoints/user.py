from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import Provide, inject

from schemas.user import UserDTO, UserCreateDTO, UserUpdateDTO
from services.user import UserService
from core.container import Container

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{user_id}", response_model=UserDTO)
@inject
async def get_user(user_id: int, service: UserService = Depends(Provide[Container.user_service])):
    return await service.get_by_id(user_id)


@router.post("", response_model=UserDTO, status_code=status.HTTP_201_CREATED)
@inject
async def create_user(
    user: UserCreateDTO,
    service: UserService = Depends(Provide[Container.user_service])
):
    return await service.create(user)


@router.patch("/{user_id}", response_model=UserDTO, status_code=status.HTTP_200_OK)
@inject
async def update_user(
    user_id: int,
    user: UserUpdateDTO,
    service: UserService = Depends(Provide[Container.user_service]),
):
    return await service.update(model_id=user_id, dto=user)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_user(user_id: int, service: UserService = Depends(Provide[Container.user_service])):
    await service.delete(model_id=user_id)
