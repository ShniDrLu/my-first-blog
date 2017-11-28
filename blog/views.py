""" view, или представление, — это то место, где мы разместим «логику» работы нашего приложения.
 Оно запросит информацию из модели, которую мы создали ранее, и передаст её в шаблон """

from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html', {})