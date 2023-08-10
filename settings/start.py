from fastapi import Depends, FastAPI

from common.parser.http import get_query_token, get_token_header
from auth.user import user

# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()


app.include_router(user.router)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


@app.get("/")
async def root():
    print("request came to me..")
    return {"message": "Hello User Service!"}
