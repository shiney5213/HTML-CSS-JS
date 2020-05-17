from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name = 'TITLE', max_length = 50)
    # 슬러그: 포스트를 설명하는 핵심 단어 집합, pk로 주로 사용
    slug = models.SlugField('SLUG', unique = True, allow_unicode = True, help_text = 'one word for title alieas')
    description = models.CharField('DESCRIPTION', max_length = 100, blank = True, help_text = 'simple descrition text')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now = True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)

    def __str__(self):
        '''
        객체의 문자열을 객체.title 속성으로 표시
        '''
        return self.title

    def get_absolute_url(self):
        '''
        메소드가 정의된 객체를 지칭하는 url 반환
        '''
        # reverse: url 패턴을 만들어주는 함수
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous(self):
        '''
        modify_dt컬럼을 기준으로 최신 포스트를 반환하는 함수
        '''
        return self.get_previous_by_modify_dt()

    def get_next(self):
        '''
        modyfy_dt 컬럼을 기준으로 다음 ㅍ포스트를 반환
        '''
        return self.get_next_by_modify_dt()