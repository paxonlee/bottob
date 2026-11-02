from logging import getLogger

from discord import Interaction, app_commands

logger = getLogger(__name__)


@app_commands.command()
async def hi(interaction: Interaction) -> None:
    """Say hi to the bot."""
    user = interaction.user
    logger.info(f"{user.name} → /hi")
    await interaction.response.send_message(f"Hi :wave:, {user.display_name}!")
