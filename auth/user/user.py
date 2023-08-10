from fastapi import APIRouter

router = APIRouter()


@router.get("/user/{id}/")
async def read_root(id: int):
    return {"User_ID": id}