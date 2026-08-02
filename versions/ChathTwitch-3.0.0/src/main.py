import sys
import os
import threading

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'packages'))

from app import create_app
from packages.web_window.window import run_window

def main():
    app, socketio = create_app()

    def run_flask():
        socketio.run(app, host='127.0.0.1', port=5001, debug=False, use_reloader=False, allow_unsafe_werkzeug=True)

    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Путь к иконке
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icon.ico')

    run_window('http://127.0.0.1:5001',
               title='TwitchAssist',
               width=1200,
               height=800,
               icon_path=icon_path)   # ← добавлено

if __name__ == '__main__':
    main()