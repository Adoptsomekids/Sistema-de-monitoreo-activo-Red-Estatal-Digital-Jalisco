import subprocess
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='5559680053:AAHUGPBqwaoba6Ek-qCS3AwDSrTZYoXo4h8')
dp = Dispatcher(bot)

button_temp = InlineKeyboardButton(text="Temperatura", callback_data="Temp")
button_rdp_ssh = InlineKeyboardButton(text="Verificar RDP/SSH", callback_data="RDP_SSH")
button_service = InlineKeyboardButton(text="Verificar servicio SLA", callback_data="Service")
button_ip = InlineKeyboardButton(text="Información IP", callback_data="IP")
keyboard_inline = InlineKeyboardMarkup().add(button_temp).add(button_rdp_ssh).add(button_service).add(button_ip)

@dp.message_handler(commands=['start', 'help', 'INICIO', 'Inicio', 'inicio'])
async def welcome(message: types.Message):
    await message.reply("¡Bienvenido al bot de monitoreo activo! ¿Qué información deseas consultar?", reply_markup=keyboard_inline)

@dp.callback_query_handler(lambda query: query.data == 'Temp')
async def query_temperature(query: types.CallbackQuery):
    output = subprocess.check_output("./commands.sh temp", shell=True)
    await query.answer(f"La temperatura actual es: {output.decode('utf-8')}", show_alert=True)

@dp.callback_query_handler(lambda query: query.data == 'RDP_SSH')
async def query_rdp_ssh(query: types.CallbackQuery):
    output = subprocess.check_output("./commands.sh rdp_ssh", shell=True)
    await query.answer(f"Estado del protocolo RDP y SSH:\n{output.decode('utf-8')}", show_alert=True)

@dp.callback_query_handler(lambda query: query.data == 'Service')
async def query_service(query: types.CallbackQuery):
    output = subprocess.check_output("./commands.sh service", shell=True)
    await query.answer(f"Estado del servicio 'sla.service':\n{output.decode('utf-8')}", show_alert=True)

@dp.callback_query_handler(lambda query: query.data == 'IP')
async def query_ip(query: types.CallbackQuery):
    output = subprocess.check_output("./commands.sh ip", shell=True)
    await query.message.answer(f"Información de direccionamiento IP:\n{output.decode('utf-8')}")

if __name__ == '__main__':
    executor.start_polling(dp)
