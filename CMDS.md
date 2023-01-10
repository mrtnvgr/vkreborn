<details>
<summary>Команды</summary>

  - `admins` - список администраторов беседы

  - `fixlayout` - изменение раскладки текста
    > Идея взята с программы [Punto Switcher](https://yandex.ru/soft/punto/win/)

  - `roll` - генератор случайных чисел/ответов
    
    - Примеры использования:
      - `roll`
        > Случайное число от 1 до 100
      - `roll 7-27` (`roll <start:int>-<end:int>`)
        > Случайное число из промежутка чисел
      - `roll foo, bar, baz, "Item with spaces"` (`roll <items:list>`)
        > Случайный элемент из списка
    
  - `shazam` - определение аудио
    > Работает на музыке и голосовых сообщениях \
    > (Также учитываются и ответы на сообщения содержащие вложения) \
    > Бэкенд: [Shazam](http://shazam.com) ([shazamio](dotX12/ShazamIO))
  
  - `trans` - перевод текста сообщений
    > (Язык текста определяется автоматически) \
    > Бэкенд: [Google Translate](https://translate.google.com) ([async-google-trans-new](sevenc-nanashi/async-google-trans-new))
    
    - Примеры использования:
      - `trans`
        > Перевод текста на английский
      - `trans de` (`trans <lang_code>`)
        > Перевод текста на немецкий
  
  - `whoami` - роль пользователя в беседе
  
</details>
