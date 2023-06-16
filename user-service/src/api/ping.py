from fastapi import APIRouter

router = APIRouter(prefix='/users/api')

@router.get("/v1/health-check")
async def ping():
    return {"hello": "world"}