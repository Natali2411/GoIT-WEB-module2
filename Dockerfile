FROM python:3.10.9
ENV APP_HOME /bot_helper
WORKDIR $APP_HOME
COPY . .
RUN pip install poetry
# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install
CMD ["python", "bot_helper/bot.py"]