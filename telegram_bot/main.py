from Bot.app import dp, bot
import asyncio


async def main() -> None:
    """
    Запуск бота без прерывания
    """

    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    
    # Асинхронный запуск
    asyncio.run(main())
