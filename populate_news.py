import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django

django.setup()
from news.models import Article


def populate():
    articles = [{'title': "Jade is angry", 'date_published': "2021-04-20 12:40:59",
                 'content': "It has now been confirmed Jade is angry"},{'title': "Matt is amazing", 'date_published': "2021-04-20 12:30:59",
                 'content': "It is official"}]

    for article in articles:
        a = Article.objects.get_or_create(title=article["title"], date_published=article["date_published"],
                                          content=article["content"])[0]
        a.save()


if __name__ == '__main__':
    print('Populating...')
    populate()
