[![Tests(+Linter)](https://github.com/Kem0111/Excel-To-Huntflow/actions/workflows/importer.yml/badge.svg)](https://github.com/Kem0111/Excel-To-Huntflow/actions/workflows/importer.yml) <a href="https://codeclimate.com/github/Kem0111/Excel-To-Huntflow/maintainability"><img src="https://api.codeclimate.com/v1/badges/84e315bc1f4e53349220/maintainability" /></a> <a href="https://codeclimate.com/github/Kem0111/Excel-To-Huntflow/test_coverage"><img src="https://api.codeclimate.com/v1/badges/84e315bc1f4e53349220/test_coverage" /></a>

# Excel-To-Huntflow

Excel-To-Huntflow это проект, который позволяет автоматизировать процесс загрузки данных о кандидатах из Excel файла в систему HuntFlow.

## Основные функции

- Парсинг данных из Excel файла.
- Поиск резюме кандидата в указанной директории.
- Загрузка резюме кандидата в систему HuntFlow.
- Создание кандидата в системе HuntFlow с соответствующими данными.
- Привязка кандидата к вакансии с указанным статусом и комментарием.

## Как использовать?


### Установка


- Введиде в командной строке:
```
python3 -m pip install --user git+https://github.com/Kem0111/Excel-To-Huntflow.git
```

- Запустите скрипт, передав токен и путь к директории с файлами:

```
import_to_huntflow --token YOUR_TOKEN --path PATH/TO/DIRECTORY
```


где YOUR_TOKEN - это ваш токен для доступа к API HuntFlow, а /PATH/TO/DIRECTORY - это путь к директории, содержащей Excel файл и резюме кандидатов.
Скрипт автоматически обработает данные из Excel файла и загрузит соответствующие резюме в систему HuntFlow.


## Ошибки и исключения

Если в процессе работы скрипта возникает ошибка, он автоматически сохраняет текущую позицию и прерывает выполнение. При следующем запуске скрипт продолжит работу с места, на котором он остановился.


### Если захотите установить скрипт локально и протестировать:

```
git clone https://github.com/Kem0111/Excel-To-Huntflow.git
```

В дирректории с установленным проектом введите следующие команды в командной строке:
```
pip install poetry
poetry install
make test-cov
```

так же можете запустить скрипт локально в корне дирректории с проектом следующей командой:

```
poetry run import_to_huntflow --token YOUR_TOKEN --path /PATH/TO/DIRECTORY
```