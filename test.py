import json
import requests
import pytest


def test_get_news():
    response = requests.get("http://0.0.0.0:8080/")
    response_body = response.json()

    assert response_body["news"][0]["id"] == 4
    assert response_body["news"][0]["comments_count"] == 1

    assert response_body["news"][1]["id"] == 3
    assert response_body["news"][1]["comments_count"] == 2

    assert response_body["news"][2]["id"] == 8
    assert response_body["news"][2]["comments_count"] == 2

    assert response_body["news"][3]["id"] == 7
    assert response_body["news"][3]["comments_count"] == 1

    assert response_body["news"][4]["id"] == 1
    assert response_body["news"][4]["comments_count"] == 3

    assert response_body["news_count"] == 5

def test_get_news_id(id):
   
    if id == 1:
        response = requests.get("http://0.0.0.0:8080/news/1")
        response_body = response.json()
        
        assert len(response_body["news"]) == 1
        assert response_body["news"][0]["id"] == id
        assert response_body["news"][0]["comments"][0]["id"] == 6
        assert response_body["news"][0]["comments"][1]["id"] == 1
        assert response_body["news"][0]["comments"][2]["id"] == 5
        assert response_body["news"][0]["comments_count"] == 3

    elif id == 2:
        response = requests.get("http://0.0.0.0:8080/news/2")
        response_body = response.json()
        assert len(response_body) == 1
        assert response_body["Error"] == "Ошибка 404"

    elif id == 3:
        response = requests.get("http://0.0.0.0:8080/news/3")
        response_body = response.json()
        assert len(response_body["news"]) == 1
        assert response_body["news"][0]["id"] == id
        assert response_body["news"][0]["comments"][0]["id"] == 13
        assert response_body["news"][0]["comments"][1]["id"] == 3
        assert response_body["news"][0]["comments_count"] == 2


    elif id == 4:
        response = requests.get("http://0.0.0.0:8080/news/4")
        response_body = response.json()
        assert len(response_body["news"]) == 1
        assert response_body["news"][0]["id"] == id
        assert response_body["news"][0]["comments"][0]["id"] == 4
        assert response_body["news"][0]["comments_count"] == 1


    elif id == 5:
        response = requests.get("http://0.0.0.0:8080/news/5")
        response_body = response.json()
        assert len(response_body) == 1
        assert response_body["Error"] == "Ошибка 404"

    elif id == 6:
        response = requests.get("http://0.0.0.0:8080/news/6")
        response_body = response.json()
        assert len(response_body) == 1
        assert response_body["Error"] == "Ошибка 404"

    elif id == 7:
        response = requests.get("http://0.0.0.0:8080/news/7")
        response_body = response.json()
        assert len(response_body["news"]) == 1
        assert response_body["news"][0]["id"] == id
        assert response_body["news"][0]["comments"][0]["id"] == 9
        assert response_body["news"][0]["comments_count"] == 1

    elif id == 8:
        response = requests.get("http://0.0.0.0:8080/news/8")
        response_body = response.json()
        assert len(response_body["news"]) == 1
        assert response_body["news"][0]["id"] == id     
        assert response_body["news"][0]["comments"][0]["id"] == 14
        assert response_body["news"][0]["comments"][1]["id"] == 10
        assert response_body["news"][0]["comments_count"] == 2
 

    elif id == 9:
        response = requests.get("http://0.0.0.0:8080/news/9")
        response_body = response.json()
        assert len(response_body) == 1
        assert response_body["Error"] == "Ошибка 404"




test_get_news()
test_get_news_id(1)
test_get_news_id(2)
test_get_news_id(3)
test_get_news_id(4)
test_get_news_id(5)
test_get_news_id(6)
test_get_news_id(7)
test_get_news_id(8)
test_get_news_id(9)