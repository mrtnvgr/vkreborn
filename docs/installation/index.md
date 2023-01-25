#### **Гайд по установке и настройке**
<br>

#### **Установка**:
```console
pip install poetry
git clone https://github.com/mrtnvgr/vkreborn
cd vkreborn
poetry install
```


#### **Настройка**:
Программа читает настройки из переменных окружения. \
Для Linux систем (`run.sh`), можно использовать `.env` (`.env.example`).


#### **Запуск (Linux)**:
```console
./run.sh
```


#### **Зависимости**:
- **PostgreSQL**
- [SoX](https://sox.sourceforge.net/) (для аудио эффектов)
