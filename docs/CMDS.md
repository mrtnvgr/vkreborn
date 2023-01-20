<details>
<summary>Команды</summary>
  
  <br>

  - `admins` - список администраторов беседы
	
  <br>

  - `fixlayout` - изменение раскладки текста
    > Спасибо [Punto Switcher](https://yandex.ru/soft/punto/win/)!

  <br>

  - `roll` - генератор случайных чисел/ответов
 
    - Примеры использования:
      - `roll`
        > Случайное число от 1 до 100
      - `roll 7-27` (`roll <start:int>-<end:int>`)
        > Случайное число из промежутка чисел
      - `roll foo, bar, baz, "Item with spaces"` (`roll <items:list>`)
        > Случайный элемент списка
	
  <br>

  - `shazam` - определение аудио
    > Поддерживаемые типы вложений: музыка, голосовые сообщения \
    > Бэкенд: [Shazam](http://shazam.com) ([shazamio](dotX12/ShazamIO))
  
  <br>

  - `trans` - перевод текста сообщений
    > Список доступных языков: [тут](https://cloud.google.com/translate/docs/languages) \
    > Бэкенд: [Google Translate](https://translate.google.com) ([async-google-trans-new](sevenc-nanashi/async-google-trans-new))

    - Примеры использования:
      - `trans`
        > Перевод текста на английский язык
      - `trans de` (`trans <lang_code>`)
        > Перевод текста на немецкий язык
  
  <br>

  - `wh` - отправка картинок с сайта [wallhaven](https://wallhaven.cc)
    > Официальная документация: [тут](https://wallhaven.cc/help/api)

    - Примеры использования:
	  - `wh`
	  - `wh Abstract` (`wh <query>`)
        > Картинка по запросу "Abstract"
	  - `wh Abstract 100` (`wh <q> <categories:wh_switches>`)
        > Картинка по запросу "Abstract", категория "General"
	  - `wh Abstract 100 100` (`wh <q> <categories:wh_switches> <purity:wh_categories>`)
	    > Картинка по запросу "Abstract", категория "General", только SFW
  
  <br>

  - `whoami` - роль пользователя в беседе
  
  <br>

  - `whreset` - очистка кэша чата команды `wh`
  > NOTE: Работает только в личных сообщениях \
	> (для использования в беседах, требуются права администратора)
  
  <br>

  - `muted` - список замьюченных в беседе
  
  <br>

  - `mutedby` - список замьюченных в беседе конкретным администратором

    - Примеры использования:
       - `mutedby @id1` (`mutedby <user:mention>`)
  
  <br>

  - `help` - ссылка на этот файл
  
  <br>

</details>

<details>
<summary>Команды для администраторов бесед</summary>
  
  <br>

  - `giveadmin` - добавление пользователя в администраторы беседы

    - Примеры использования:
      - `giveadmin @id1` (`giveadmin <user:mention>`)
  
  <br>

  - `kick` - исключение пользователя из беседы

    - Примеры использования:
      - `kick @id1` (`kick <user:mention>`)
  
  <br>

  - `invite` - приглашение пользователя в беседу

    - Примеры использования:
      - `invite @id1` (`invite <user:mention>`)
  
  <br>

  - `forceinvite` - форсированное приглашение пользователя в беседу
    > Сработает если у пользователя разрешены приглашения в настройках приватности
  
  <br>

  - `mute` - автоматическое удаление сообщений пользователя

    - Примеры использования:
      - `mute @id1 30` (`mute <user:mention> <minutes:float>`)
        > Мут пользователя @id1 на 30 минут
  
  <br>

  - `unmute` - отмена действия команды `mute` на пользователя

    - Примеры использования:
      - `unmute @id1` (`unmute <user:mention>`)
  
  <br>

  - `takeadmin` - удаление пользователя из администраторов беседы

    - Примеры использования:
      - `takeadmin @id1` (`takeadmin <user:mention>`)
  
  <br>

  - `whreset` - очистка кэша команды `wh` в беседе
  
  <br>

</details>

<details>
<summary>Команды для овнера</summary>
  
  <br>

  - `whgreset` - очистка кэша команды `wh` глобально
  
  <br>

</details>

> NOTE: знаки <> являются пояснениями аргумента команды \
> В формате: <название:тип> \
> (команды без примеров использования не принимают аргументов)
