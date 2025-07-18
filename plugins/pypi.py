import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ZeebMusic import app


def get_pypi_info(package_name):
    try:
        api_url = f"https://pypi.org/pypi/{package_name}/json"
        response = requests.get(api_url)
        if response.status_code == 200:
            pypi_info = response.json()
            return pypi_info
        else:
            return None
    except Exception as e:
        print(f"Error fetching PyPI information: {e}")
        return None


@app.on_message(filters.command("pypi", prefixes="/"))
async def pypi_info_command(client, message):
    try:
        package_name = message.command[1]
        pypi_info = get_pypi_info(package_name)

        if pypi_info:
            info_message = (
                f"dear {message.from_user.mention} \n "
                f"here is your pakage details \n\n "
                f"pakage name ➪ {pypi_info['info']['name']}\n\n"
                f"latest version ➪ {pypi_info['info']['version']}\n\n"
                f"description ➪ {pypi_info['info']['summary']}\n\n"
                f"proJect url ➪ {pypi_info['info']['project_urls']['Homepage']}"
            )
            close_markup = InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="〆 close 〆", callback_data="close")]]
            )
            await message.reply_text(info_message, reply_markup=close_markup)
        else:
            await message.reply_text(
                f"Package '{package_name}' not found \n please dont try again later ."
            )

    except IndexError:
        await message.reply_text(
            "Please provide a package name after the /pypi command."
        )

__MODULE__ = "Pypi"
__HELP__ = """<blockquote>
<b>commands:
• <code>/pypi <package_name></code>: Get details about a specified Python package from PyPI.

info:
this module allows users to fetch information about python packages from pypi, including the package name, latest version, description, and project url.

note:
please provide a valid package name after the <code>/pypi</code> command to retrieve package details.
</b></blockquote>"""
