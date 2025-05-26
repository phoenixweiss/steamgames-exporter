import os
import argparse
import requests
import pandas as pd
from dotenv import load_dotenv

# Загружаем переменные из .env файла, если он есть
load_dotenv()

def fetch_owned_games(api_key, steam_id):
    # Формируем URL запроса к Steam API
    url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
    params = {
        'key': api_key,
        'steamid': steam_id,
        'include_appinfo': 1,  # получить названия игр
        'include_played_free_games': 1,
        'format': 'json'
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get('response', {}).get('games', [])

def save_to_csv(games, filename):
    if not games:
        print("No games found or profile is private.")
        return

    df = pd.DataFrame(games)
    df['playtime_hours'] = (df['playtime_forever'] / 60).round(2)
    df = df[['appid', 'name', 'playtime_hours']]
    df.columns = ['App ID', 'Game Name', 'Playtime (h)']
    df.sort_values(by='Playtime (h)', ascending=False).to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"Exported {len(df)} games to {filename}")

def save_to_json(games, filename):
    if not games:
        print("No games found or profile is private.")
        return

    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(games, f, ensure_ascii=False, indent=2)
    print(f"Exported {len(games)} games to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Export your Steam game library to CSV or JSON.")
    parser.add_argument('--steamid', help="Your 64-bit Steam ID")
    parser.add_argument('--apikey', help="Your Steam Web API key")
    parser.add_argument('--format', choices=['csv', 'json'], default='csv', help="Output format (default: csv)")
    parser.add_argument('--output', help="Output filename (optional)")

    args = parser.parse_args()

    # Получение данных из .env, если аргументы не переданы
    steam_id = args.steamid or os.getenv('STEAM_ID')
    api_key = args.apikey or os.getenv('STEAM_API_KEY')

    if not steam_id or not api_key:
        print("Error: you must provide steamid and apikey via arguments or a .env file.")
        return

    games = fetch_owned_games(api_key, steam_id)
    output_file = args.output or f"steam_games.{args.format}"

    if args.format == 'csv':
        save_to_csv(games, output_file)
    else:
        save_to_json(games, output_file)

if __name__ == "__main__":
    main()
