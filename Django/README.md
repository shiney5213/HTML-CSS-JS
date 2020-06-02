#  Django

---

## 1. csrf 403 forbidden Error

#### 1.1. html의 form에서 처리
```
 <form action='videoedit' enctype="multipart/form-data" method = 'POST'>
        {% csrf_token %}
        <input type = 'file' name = 'filename'>
        <input type = 'submit' value = 'upload'>
</form>
```

#### 1.2. django에서 함수에서 처리
```
@csrf_exempt
 def download(request):
     global filename, file
     print(request.POST.keys())
     ...
```

#### 1.3. django에서 class에서 처리
```
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class downloadView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(downloadView, self).dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, 'highlight/video_jquery.html')

    def post(self, request):
        starttimearray = request.POST.get('starttimearray[]', '')
        ...
```

