import os
import sys

from core.stt import SpeachToText
from core.assistant import Assistant
from core import config
from core.commands_loader import load_commands


def resolve_stt_models() -> dict | str:
    """
    Бере мови з config.yaml (assistant.stt_languages / stt_models) і
    залишає тільки ті, чия папка моделі реально існує на диску —
    щоб не падати, якщо, наприклад, українську модель ще не завантажено.
    """
    available = {}

    for lang in config.STT_LANGUAGES:
        path = config.STT_MODELS.get(lang)
        if path and os.path.isdir(path):
            available[lang] = path
        else:
            print(f"⚠ Модель для мови '{lang}' не знайдена за шляхом: {path}")

    if not available:
        # аварійний fallback, щоб асистент хоч якось запустився
        print("⚠ Жодної мовної моделі не знайдено, пробую 'models/small/vosk-ru'")
        return "models/small/vosk-ru"

    return available


def main():
    commands = load_commands()
    stt = SpeachToText(resolve_stt_models())
    assistant = Assistant(stt, commands)

    try:
        assistant.run()
    except KeyboardInterrupt:
        print("Stoped 🔴")
        sys.exit(0)

    finally:
        stt.stop()


if __name__ == "__main__":
    main()
