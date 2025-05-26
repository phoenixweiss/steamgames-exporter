# steamgames-exporter

[Switch to English](./README.md)

**steamgames-exporter** — это лёгкая в использовании CLI-утилита для экспорта библиотеки игр Steam с помощью официального Steam Web API. Результат может быть сохранён в формате CSV или JSON.

Проект с открытым исходным кодом. В будущем может быть расширен до графического интерфейса.

## Возможности

- Получение списка всех приобретённых игр
- Вывод количества отыгранных часов
- Экспорт данных в CSV или JSON
- Работа через Steam Web API без входа в аккаунт

## Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/phoenixweiss/steamgames-exporter.git
cd steamgames-exporter
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

## Получение Steam ID и API-ключа

1. Получите **Steam API Key**:
   `https://steamcommunity.com/dev/apikey`

2. Получите **SteamID64**:
   - Если ваш профиль в формате `https://steamcommunity.com/id/yourname`,
     перейдите на `https://steamid.io` и введите имя, чтобы получить SteamID64.
   - Если адрес вида `https://steamcommunity.com/profiles/76561198012345678`,
     используйте это значение как SteamID.

## Использование

```bash
python steam_export.py --steamid YOUR_STEAM_ID --apikey YOUR_API_KEY --format csv
```

### Аргументы

| Аргумент     | Описание                                  |
|--------------|--------------------------------------------|
| `--steamid`  | Ваш SteamID64                              |
| `--apikey`   | Ключ Web API от Steam                      |
| `--format`   | Формат вывода: `csv` (по умолчанию) или `json` |
| `--output`   | Имя выходного файла (необязательно)        |

### Пример

```bash
python steam_export.py --steamid 76561198012345678 --apikey ABCDEFG123456789 --format csv --output my_games.csv
```

### Использование файла .env вместо аргументов командной строки

Можно сохранить данные в файле `.env` в корне проекта:

```env
STEAM_ID=ваш_steam_id
STEAM_API_KEY=ваш_api_key
```

После этого достаточно выполнить:

```bash
python steam_export.py
```

## План развития

- [x] Базовая CLI-утилита
- [ ] Экспорт дополнительных метаданных (жанры и др.)
- [ ] Графический интерфейс
- [ ] Автоматическое определение SteamID по URL

## Лицензия

Проект распространяется под лицензией MIT. См. файл `LICENSE`.

## Контрибьютинг

Приветствуются улучшения, исправления и предложения. Открывайте issues или pull request.
