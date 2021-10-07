from django.shortcuts import render
import requests

# # Create your views here.
# def home(requests):
#     form = Url(requests.POST)
#     key = "1b13f5d1aa58786f36b0e41ed2157a29415df"
#     form = Url()
#     url = UrlData.url
#     api_url = f"https://cutt.ly/api/api.php?key={key}&short={url}"
#     data = requests.GET.get(api_url).json()["url"]
#     if data["status"] == 7:
#         shortened_url = data["shortLink"]
#     else:
#         shortened_url = "Error! Link to short."

#     context = {
#         'form' : form,
#         'shortened_url' : shortened_url
#     }

#     return render(requests, 'UrlShortApp/home.html', context)

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