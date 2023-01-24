#### Гайд по установке и настройке
<br>

#### Установка
```console
git clone https://github.com/mrtnvgr/vkreborn
cd vkreborn
poetry install
```


#### Настройка
Программа читает настройки из переменных окружения. \
Для Linux систем (`run.sh`), можно использовать `.env` (`.env.example`).


#### Запуск (Linux)
```console
./run.sh
```


#### Сторонние зависимости
- Любая SQL БД
- [SoX](https://sox.sourceforge.net/) (для аудио эффектов)
