# Simon Says / 西蒙说

A bilingual console memory sequence game written with the Python standard library.

一个使用 Python 标准库编写的双语控制台记忆序列小游戏。

## Features / 功能

- Memorize and repeat growing color sequences.
- Accepts full color names or shortcuts: `r`, `b`, `g`, `y`.
- Three difficulty levels: easy, normal, hard.
- Bilingual UI: English and Chinese.
- Persistent JSON settings and top scores.
- Optional terminal bell sound with adjustable volume.
- Automated tests for core logic, persistence modules, sound, and menu gameplay.

## Requirements / 环境要求

- Python 3.9+
- No third-party dependencies.

## Run / 启动

```bash
python3 game.py
```

## Test / 测试

```bash
python3 -m py_compile game.py simon_says.py i18n.py settings.py score.py sound.py
python3 tests/run_tests.py
```

## How to Play / 玩法

1. Choose Play from the main menu.
2. Watch the sequence shown after `Simon says`.
3. Type the sequence back in order, separated by spaces or commas.
4. You can use full names (`red blue`) or shortcuts (`r b`).
5. Type `hint` once per round to reveal the first color and length.
6. Type `q` to quit the current round.

## Difficulty / 难度

| Difficulty | Rounds | Start length | Score bonus |
| --- | ---: | ---: | ---: |
| easy | 6 | 1 | 1x |
| normal | 8 | 2 | 2x |
| hard | 10 | 3 | 3x |

## Files / 文件

- `game.py` — console UI and menus.
- `simon_says.py` — core sequence and scoring logic.
- `i18n.py` — bilingual strings.
- `settings.py` — JSON settings persistence.
- `score.py` — JSON score persistence.
- `sound.py` — terminal bell sound helper.
- `tests/` — automated unit tests.
