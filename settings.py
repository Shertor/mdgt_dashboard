from pydantic import BaseSettings
import os
from sys import platform

if platform == "linux" or platform == "linux2":
    statment_path = "/run/user/1000/gvfs/smb-share:server=192.168.0.1,share=files/МДГТ - (Учет рабоч. времени, Отпуск, Даты рожд., телефоны, план работ)/ПРОТОКОЛЫ+ведомости.xls"
    prize_dir = "/run/user/1000/gvfs/smb-share:server=192.168.0.1,share=files/МДГТ - (Учет рабоч. времени, Отпуск, Даты рожд., телефоны, план работ)/УЧЕТ рабочего времени/"
elif platform == "win32":
    statment_path = "//192.168.0.1/files/МДГТ - (Учет рабоч. времени, Отпуск, Даты рожд., телефоны, план работ)/ПРОТОКОЛЫ+ведомости.xls"
    prize_dir = "//192.168.0.1/files/МДГТ - (Учет рабоч. времени, Отпуск, Даты рожд., телефоны, план работ)/УЧЕТ рабочего времени/"

class Settings(BaseSettings):
    server_host: str = "127.0.0.1"
    server_port: int = 8001
    statment_excel_path: str = os.path.normpath("/run/user/1000/gvfs/smb-share:server=192.168.0.1,share=files/МДГТ - (Учет рабоч. времени, Отпуск, Даты рожд., телефоны, план работ)/ПРОТОКОЛЫ+ведомости.xls")
    prize_directory: str = os.path.normcase("/run/user/1000/gvfs/smb-share:server=192.168.0.1,share=files/МДГТ - (Учет рабоч. времени, Отпуск, Даты рожд., телефоны, план работ)/УЧЕТ рабочего времени/")
    database_url: str = "sqlite:///./db/database.sqlite3"

    jwt_secret: str = "OOIOIPSJFBSFBSBGBBSB"
    jwt_algorithm: str = "HS256"
    jwt_expiration: int = 3600


settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8"
)