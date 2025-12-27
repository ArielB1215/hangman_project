FROM python:3.13

COPY game_functions/. game_functions/

COPY main_game.py .

COPY common/. common/

CMD ["python3",  "main_game.py"]