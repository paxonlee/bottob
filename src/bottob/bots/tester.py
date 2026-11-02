import os
from logging import getLogger

from discord import Client, Intents, Object
from discord.app_commands import CommandTree
from discord.utils import setup_logging

from bottob.commands.hi import hi

logger = getLogger(__name__)


class Tester(Client):
    def __init__(self, guild_id: int) -> None:
        super().__init__(intents=Intents.default())
        self.guild = Object(id=guild_id)
        self.tree = CommandTree(self)
        self.tree.add_command(hi, guild=self.guild)

    async def setup_hook(self) -> None:
        commands = await self.tree.sync(guild=self.guild)
        logger.info(f"Synced commands: {', '.join(c.name for c in commands)}")

    async def on_ready(self) -> None:
        logger.info(f"{self.user} is ready!")


def main() -> None:
    setup_logging()
    bot = Tester(guild_id=int(os.environ["GUILD_ID"]))
    bot.run(os.environ["TESTER_BOT_TOKEN"], log_handler=None)


if __name__ == "__main__":
    main()
