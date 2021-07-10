#Сначала нужно установить эти пакеты, чтоб заработало. Напротив каждой библиотеки кроме стандартных питоновских инструкция, 
# что ввести в командную строку\терминал в VS Code чтоб установить
#Кстати, спецсимвол \n-это просто перенос строки

import re
import pyglet
import vk_api #pip install vk_api
from PIL import Image #pip install Pillow
import matplotlib.pyplot as plt #pip install matplotlib
import requests
import vlc  #pip install vlc


def playMusic(playMusicItemFromWall):
    try: 
        playMusicUrl = playMusicItemFromWall['attachments'][0]['audio']['url']
        p = vlc.MediaPlayer(playMusicUrl)
        p.play()
        v = input()#Если убрать это-то программа просто завершится) А аудио не прогрузится, и не воспроизведётся.
        
    except:
        print("Ну не получилось объект получить хуль\n Объект который пришёл:\n", playMusicItemFromWall)
        return


#сначала определяем функции, их нужно определить до вызова(вызов внизу)
def auth_handler(): #Cюда не лезть, сложна
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    key = input("Код аутентификации(если в вк включён то пришёл либо в ЛС либо на телефон): \n")#input-это просто запрос строки у пользователя(в терминале нужно тыкнуть и ввести)
    # Если: True - сохранить браузер, False - не сохранять.
    remember_device = True

    return key, remember_device

def image_show_handler(response): #функция отображения картинки из 
    try:
        print(response)
        if response['items'][0]['copy_history'][0]['attachments'][0]['photo']['sizes'][7]['url']:
            url = response['items'][0]['copy_history'][0]['attachments'][0]['photo']['sizes'][7]['url']
            img = Image.open(requests.get(url, stream=True).raw)
            imgplot = plt.imshow(img)
            plt.show()

    except:
        print("Ну не получилось объект получить хуль\n Объект который пришёл:\n", response)
        return

def main():
    login, password = "", ""
    #login, password = input("Логин/телефон от вк:\n"), input('пароль:\n') #Обявляется сразу 2 переменных, и задаются значения для них. 
    #Можно чтоб не долбиться в очко постоянно написать так: login, password = "ТутТвойЛогин", "ТутТвойПароль"
    #login, password = input(), input('пароль:\n')
    #Но следите, чтоб не отправить случайно свои изменения, после использования верните как было, а то пароль будет скомпроментирован)
    vk_session = vk_api.VkApi(
        login, password,        
        auth_handler=auth_handler # функция для обработки двухфакторной аутентификации которая возвращает код и необходимость "запомнить" этот "браузер" (имитируется firefox)
    )

    try:
        vk_session.auth() #авторизует тебя 
        vk = vk_session.get_api() #включает api и задаёт ему переменную (vk)
        response = vk.wall.get(count=2, owner_id=26377560)  #Используя vk api получаем первую запись со стены керила (документация по api вот тут https://vk.com/dev/wall.get)
        image_show_handler(response) #вызывается функция сверху (нажми ctrl+ЛКМ чтоб перейти к ней)

        playMusic(response['items'][1])
        #print(response) #тупо выводим что вернул метот
        #print('Ну всё типо')

    except vk_api.AuthError as error_msg:
        print(error_msg) #вывод ошибки, если не удалось авторизоваться
        return
    except:
        print("Не падой пажалуста")


