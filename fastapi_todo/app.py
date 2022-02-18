from fastapi import FastAPI

from fastapi_todo.views.todo_views import todo_router
from fastapi_todo.views.user_views import user_router

PREFIX = "/api/v1"

app = FastAPI(openapi_url="/openapi.json")

app.router.prefix = PREFIX

app.include_router(user_router, prefix="/users")
app.include_router(todo_router, prefix="/todos")
