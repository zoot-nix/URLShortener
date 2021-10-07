from django.shortcuts import render
import requests

def home(request):
    return render(request, 'UrlShortApp/base.html')

def result(request):
    start_url = request.POST['my_url']
    key = "1b13f5d1aa58786f36b0e41ed2157a29415df"
    api_url = f"https://cutt.ly/api/api.php?key={key}&short={start_url}"
    data = requests.get(api_url).json()["url"]
    if data["status"] == 7:
        final_url = data["shortLink"]
    else:
        final_url = "Error! Link to short."

    context = {
        'final_url' : final_url,
        'start_url' : start_url
    }


    return render (request, 'UrlShortApp/result.html', context)
