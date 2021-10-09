from aiohttp import web
from aiohttp.web_request import Request
import json
from datetime import datetime

class Handler:
    def __init__(self):
        pass

    async def handler_news(self, request, path_news = "news.json", path_comm = "comments.json"):
        data_news = json.load(open(path_news))
        data_comments = json.load(open(path_comm))
        null_values = {"null", ""}

        #Сортировка по дате убираем ненужные записи
        for i in data_news['news']:
            i["date"] = datetime.strptime(i["date"], '%Y-%m-%dT%H:%M:%S')
        data_news['news'] = sorted((item for item in data_news["news"] if (item["date"] not in null_values)  
                                    and (item["deleted"] != True) and (item["date"]<=datetime.today())),
                                    key=lambda x: x["date"], reverse=True)

        #Находим количество новостей
        count_news = 0
        for i in data_news['news']:
            i["date"] = i["date"].isoformat()
            count_news += 1
        data_news["news_count"] = count_news

        #Находим количество комментариев
        for i in data_news['news']:
            count = 0
            for j in data_comments['comments']:
                if i["id"] == j['news_id']:
                    count+=1
            i["comments_count"] = count

        return web.json_response(data_news)


    async def handler_find_news(self, request, path_news = "news.json", path_comm = "comments.json"):
        data_news = json.load(open(path_news))
        data_comments = json.load(open(path_comm))
        null_values = {"null", ""}
        additional_info = {"Error": "Ошибка 404"}

        try:
            id = int(request.match_info["id"])
        except ValueError:
            id = None
            return web.json_response(additional_info)

        #Фильтрация по id
        data_news["news"] = [item for item in data_news["news"] if item["id"] == id]
        
        #Проверка на наличие записей
        if not data_news["news"]:
            return web.json_response(additional_info)

        #Проверка условий: удалены ли записи, время создания еще не наступило
        for i in data_news["news"]:
            i["date"] = datetime.strptime(i["date"], '%Y-%m-%dT%H:%M:%S')

            if (i["deleted"] == True) or (i["date"] > datetime.today()):
                return web.json_response(additional_info)

            i["date"] = i["date"].isoformat()

        #Получаем комментарии, количество комментариев, сортировка по дате
        for i in data_news['news']:
            count = 0
            mass_com = []
            for j in data_comments['comments']:
                if  (j['news_id'] == i["id"]):
                    j["date"] = datetime.strptime(j["date"], '%Y-%m-%dT%H:%M:%S')
                    mass_com.append(j)
                    count += 1
            data_comments['comments'] = sorted((item for item in mass_com), 
                                                key=lambda x: x["date"], reverse=True)
            for d in data_comments['comments']:
                d["date"] = d["date"].isoformat()
            i["comments"] = data_comments['comments']
            i["comments_count"] = count
        del data_news["news_count"]
        return web.json_response(data_news)


handler = Handler()

app = web.Application()
app.add_routes([web.get('/', handler.handler_news),
                web.get('/news/{id}', handler.handler_find_news)])

web.run_app(app)
