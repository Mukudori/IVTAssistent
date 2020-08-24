# -*- coding: utf-8 -*-

def getText(client):

    text = "Я диалоговая система, предназначенная для информационной " \
           "поддержки клиентов. В данный момент в роли клиентов выступают " \
           "посетители сайта РИИ." \
           "\nВы можете спросить о последних новостях или просто побеседовать " \
           "написав 'давай побеседуем'." \
           "\n\nЕсли вы студент, то вы можете спросить расписание своих занятий " \
           "фразами 'Какие сегодня пары', 'какая идет неделя', 'Какое расписание на" \
           " этой неделе." \
           "\n\nЕсли вы преподаватель, то вы можете так же узнать свое расписание, " \
           "узнать свободна ли какя либо аудитория, запросить информацию о проекторах " \
           "и зарезервировать проектор, в случае если он свободен. "
    return text


def execute(args):
    '''
   Вывод списка возможностей системы
    :param args: кортеж входных параметров,
            args[0] == ссылка на класс шаблонной логики
    :return: Возвращает текстовый ответ в конце сценария
    '''
    tempLogic = args[0]
    client = tempLogic.client

    outText = getText(client)

    return outText