from django.contrib import admin
from blog.models import Post
# Register your models here.

@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    '''
    Post 클래스가 admin사이트에서 어떻게 보여줄지 정의
    '''
    # 화면에 출력할 내용
    list_display = ('id', 'title', 'modify_dt')
    # 필더 사이트바
    list_fliter = ('modify_dt',)
    # 검색박스 : 어떤 컬럼에서 검색할지 표시    
    search_filed = ('title', 'content')
    #  titie 필드를 사용해러 slug필드가 미리 채워지도록 하기
    prepopulated_fields = {'slug': ('title',)}

