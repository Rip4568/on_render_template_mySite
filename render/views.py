from django.shortcuts import render

def index(request) -> render:
    TEMPLATE_INDEX_PATH:str = "render/index.html"
    context: dict = {'request':request}
    return render(request,template_name=TEMPLATE_INDEX_PATH,context=context)


