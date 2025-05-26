# steamgames-exporter

[Перейти на русский язык](./README_RU.md)

**steamgames-exporter** is a lightweight CLI tool that exports your Steam game library using the official Steam Web API. Output can be saved as CSV or JSON.
The tool is open source and may later evolve into a GUI application.

## Features

- Fetch all owned games from your Steam library
- Show total playtime per game (in hours)
- Export to CSV or JSON
- Uses Steam Web API without login

## Installation

Clone the repository:

```bash
git clone https://github.com/phoenixweiss/steamgames-exporter.git
cd steamgames-exporter
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Get Steam ID and API Key

1. Get your **Steam API Key**:
   `https://steamcommunity.com/dev/apikey`

2. Get your **SteamID64**:
   - If your profile URL is like `https://steamcommunity.com/id/yourname`,
     visit `https://steamid.io` and enter your name to get the 64-bit SteamID.
   - If your URL is like `https://steamcommunity.com/profiles/76561198012345678`,
     use the numeric ID directly.

## Usage

```bash
python steam_export.py --steamid YOUR_STEAM_ID --apikey YOUR_API_KEY --format csv
```

### Arguments

| Argument     | Description                               |
|--------------|-------------------------------------------|
| `--steamid`  | Your 64-bit Steam ID                      |
| `--apikey`   | Your Steam Web API key                    |
| `--format`   | Output format: `csv` (default) or `json`  |
| `--output`   | Output filename (optional)                |

### Example

```bash
python steam_export.py --steamid 76561198012345678 --apikey ABCDEFG123456789 --format csv --output my_games.csv
```

### Using .env instead of command-line arguments

You can also store your credentials in a `.env` file in the root folder:

```env
STEAM_ID=your_steam_id
STEAM_API_KEY=your_api_key
```

Then simply run:

```bash
python steam_export.py
```

## Roadmap

- [x] Basic CLI tool
- [ ] Export additional metadata (genres, etc.)
- [ ] GUI support (desktop app)
- [ ] Auto-detect SteamID from profile URL

## License

Licensed under the MIT License. See `LICENSE` for details.

## Contributing

Contributions and feedback are welcome. Please open an issue or pull request.
