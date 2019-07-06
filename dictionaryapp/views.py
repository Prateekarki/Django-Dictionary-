import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def dictionary(request):
    new_result = None
    data = json.load(open("data.json"))
    data.items()

    val = request.POST.get("word")
    print(val)
    if val in data:
        result = data[val]
        new_result = result[0]
        " ".join(str(x) for x in result)
    else:
        print("Not Found")

    return render(request, "dictionaryapp/homepage.html", {"result": new_result})

