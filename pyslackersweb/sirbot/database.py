import logging

import asyncpg
import sqlalchemy as sa

from pyslackersweb import models
from pyslackersweb.util.log import ContextAwareLoggerAdapter


logger = ContextAwareLoggerAdapter(logging.getLogger(__name__))


async def is_admin(conn: asyncpg.connection.Connection, user: str) -> bool:
    return await conn.fetchval(sa.select([models.SlackUsers.c.admin]).where(id=user))
