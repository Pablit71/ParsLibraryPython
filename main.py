import requests
from bs4 import BeautifulSoup

# Получаем запрос пользователя
search_query = input("Введите название библиотеки для поиска: ")

# URL-адрес страницы PyPI для поиска
url = f"https://pypi.org/search/?q={search_query}"
# Отправляем GET-запрос и получаем HTML-код страницы
response = requests.get(url)
html = response.content

# Создаем объект BeautifulSoup для парсинга HTML-кода страницы
soup = BeautifulSoup(html, "html.parser")

# Находим первую ссылку на страницу библиотеки из списка результатов поиска на сайте PyPI
results = soup.find("ul", class_="unstyled")
if not results:
    print("Ничего не найдено.")
else:
    result_link = results.find("a", class_="package-snippet")["href"]
    result_url = f"https://pypi.org{result_link}"

    # Отправляем GET-запрос на страницу библиотеки и получаем HTML-код страницы
    response = requests.get(result_url)
    html = response.content

    # Создаем объект BeautifulSoup для парсинга HTML-кода страницы библиотеки
    soup = BeautifulSoup(html, "html.parser")

    # Получаем информацию о названии библиотеки
    package_name = soup.find("h1", class_="package-header__name").text.strip()

    # Получаем информацию о команде установки
    install_command = soup.find("span", id="pip-command").text.strip()
    # Получаем информацию описании библиотеки
    package_description = soup.find("div", class_="project-description").text.strip()

    # Выводим результаты
    print(f"Название: {package_name}")
    print(f"Команда установки: {install_command}")
    print(f"Описание: {package_description}")
