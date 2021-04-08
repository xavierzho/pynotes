"""
@Author: Jonescyna@gmail.com
@Created: 2021/3/9
"""
from main import router
from models import LoginByPhone, LoginByUsername


@router.get('/')
async def index():
    return {"index page": True}


@router.post('/login')
async def login(user: LoginByPhone):
    return {"msg": "login success", "phone": user.phone}


async def login_username(user: LoginByUsername):
    return {"msg": f"login failed,{user.username} not found"}