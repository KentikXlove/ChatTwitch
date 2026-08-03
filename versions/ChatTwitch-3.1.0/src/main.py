import sys
import os
import threading
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'packages'))

from app import create_app
from packages.web_window.window import run_window

def main():
    app, socketio = create_app()



    # Путь к иконке
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icon.ico')

    # Чтение начального значения always_on_top
    current_dir = os.path.dirname(os.path.abspath(__file__))  # .../packages/web_window
    parent_dir = os.path.dirname(current_dir)  # .../packages
    root_dir = os.path.dirname(parent_dir)  # .../TwitchChat (корень)
    config_path = os.path.join(root_dir, 'config.json')
    print(config_path)
    always_on_top = False
    print(f"существование {os.path.exists(config_path)}")
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                print(config)
                always_on_top = config.get('overlay', {}).get('always_on_top', False)
                print(config.get('overlay', {}).get('always_on_top', False))
        except Exception:
            pass

    def run_flask():
        socketio.run(app, host='127.0.0.1', port=5001, debug=False, use_reloader=False, allow_unsafe_werkzeug=True)

    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    run_window('http://127.0.0.1:5001',
               title='TwitchAssist',
               width=1200,
               height=800,
               icon_path=icon_path,
               always_on_top=always_on_top)

if __name__ == '__main__':
    main()