# (c) adarsh-goel
from pyrogram import Client
import pyromod.listen
from ..vars import Var
from os import getcwd

StreamBot = Client(
    name='Web Streamer',
    api_id=Var.21675188,
    api_hash=Var.e0a522628a13877a441327362b0cf431,
    bot_token=Var.6721837633:AAGEdUG9K5AhWdpro7z-ZXVJed-yJ_HW6tM,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)

multi_clients = {}
work_loads = {}
