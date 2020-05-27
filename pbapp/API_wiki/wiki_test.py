# -*- coding: utf-8 -*-
import requests
from json import loads

from pbapp.API_wiki.wiki import *


def test_id_article(monkeypatch):
    def fake_id_page(url, params):
        class FakeReturn():
            def json():
                results = 7785129
                return loads(results)

        return FakeReturn

    fake_results = 7785129

    monkeypatch.setattr(requests, 'get', fake_id_page)
    page_id = get_id_wiki('48.856614|2.3522219')
    assert page_id == fake_results


def test_article(monkeypatch):
    def fake_article(url, params):
        class FakeReturn():
            def json():
                results = "Les Jeux olympiques d'été de 2024, officiellement appelés les Jeux de la XXXIIIe olympiade " \
                          "de l'ère moderne, seront célébrés en 2024 à Paris, en France, officiellement désignée lors " \
                          "de la 131e session du CIO à Lima, au Pérou, le 13 septembre 2017,. Les villes de Hambourg, " \
                          "Rome, et Budapest étaient également en lice jusqu'à leurs retraits, respectivement les 29 " \
                          "novembre 2015, 11 octobre 2016 et 22 février 2017 ; et la ville de Los Angeles est désignée " \
                          "pour organiser les Jeux olympiques de 2028, conformément à l'accord trouvé avec le CIO, le " \
                          "31 juillet 2017. Après Londres (1908, 1948 et 2012), Paris devient la deuxième ville à " \
                          "célébrer les Jeux olympiques d'été pour la troisième fois, à cent ans d'écart " \
                          "(1900, 1924 et 2024), avant que ce ne soit le tour de Los Angeles (1932, 1984 et 2028). " \
                          "\nLe projet Paris 2024 s'appuie sur 95 % de sites déjà existants ou temporaires pour un " \
                          "budget annoncé de 6,6 milliards d'euros. Les seules réalisations nécessaires sont un " \
                          "centre aquatique qui doit être construit à côté du Stade de France, une arène couverte " \
                          "de 7 500 places pour le basketball et la lutte à la porte de la Chapelle, et le village " \
                          "olympique qui sortira de terre à cheval sur les trois communes de L'Île-Saint-Denis, " \
                          "Saint-Denis et Saint-Ouen-sur-Seine en Seine-Saint-Denis. Tony Estanguet, qui " \
                          "co-dirigeait l'équipe de candidature avec Bernard Lapasset, prend la présidence du " \
                          "comité d'organisation des Jeux olympiques de Paris 2024, dont le directeur général est " \
                          "Étienne Thobois. \nLe 7 février 2018, un changement dans le calendrier est annoncé. " \
                          "Les JO, qui devaient initialement se dérouler du 2 au 18 août, sont avancés d'une " \
                          "semaine pour des raisons d'organisation. Ils se tiendront finalement du 26 juillet au " \
                          "11 août 2024.\n\n"
                return loads(results)

        return FakeReturn

    fake_results = "Les Jeux olympiques d'été de 2024, officiellement appelés les Jeux de la XXXIIIe olympiade " \
                   "de l'ère moderne, seront célébrés en 2024 à Paris, en France, officiellement désignée lors " \
                   "de la 131e session du CIO à Lima, au Pérou, le 13 septembre 2017,. Les villes de Hambourg, " \
                   "Rome, et Budapest étaient également en lice jusqu'à leurs retraits, respectivement les 29 " \
                   "novembre 2015, 11 octobre 2016 et 22 février 2017 ; et la ville de Los Angeles est désignée " \
                   "pour organiser les Jeux olympiques de 2028, conformément à l'accord trouvé avec le CIO, le " \
                   "31 juillet 2017. Après Londres (1908, 1948 et 2012), Paris devient la deuxième ville à " \
                   "célébrer les Jeux olympiques d'été pour la troisième fois, à cent ans d'écart " \
                   "(1900, 1924 et 2024), avant que ce ne soit le tour de Los Angeles (1932, 1984 et 2028). " \
                   "\nLe projet Paris 2024 s'appuie sur 95 % de sites déjà existants ou temporaires pour un " \
                   "budget annoncé de 6,6 milliards d'euros. Les seules réalisations nécessaires sont un " \
                   "centre aquatique qui doit être construit à côté du Stade de France, une arène couverte " \
                   "de 7 500 places pour le basketball et la lutte à la porte de la Chapelle, et le village " \
                   "olympique qui sortira de terre à cheval sur les trois communes de L'Île-Saint-Denis, " \
                   "Saint-Denis et Saint-Ouen-sur-Seine en Seine-Saint-Denis. Tony Estanguet, qui " \
                   "co-dirigeait l'équipe de candidature avec Bernard Lapasset, prend la présidence du " \
                   "comité d'organisation des Jeux olympiques de Paris 2024, dont le directeur général est " \
                   "Étienne Thobois. \nLe 7 février 2018, un changement dans le calendrier est annoncé. " \
                   "Les JO, qui devaient initialement se dérouler du 2 au 18 août, sont avancés d'une " \
                   "semaine pour des raisons d'organisation. Ils se tiendront finalement du 26 juillet au " \
                   "11 août 2024.\n\n"

    monkeypatch.setattr(requests, 'get', fake_article)
    wiki_article = get_article_wiki(page_id=7785129)
    assert wiki_article == fake_results
