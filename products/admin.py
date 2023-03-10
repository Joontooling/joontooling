from django.contrib import admin
from .models import Products, ProductsInfo
from django.utils.safestring import mark_safe
from django.contrib.humanize.templatetags.humanize import intcomma
# Register your models here.

# admin 상품 등록

class AddInfoImage(admin.StackedInline):
    model = ProductsInfo

class InfoProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'cnt_q', 'comma_price')
    inlines = [AddInfoImage,] # 상세 설명 이미지 등록 모델 인라인 추가 설정

    fieldsets = [
        ('상품 기본 정보' , {'fields' : ['name', 'category', 'price','quantity', 'point', 'serial', 'delivery']}),
        ("메인 사진", {'fields' : ['image_main1','image_main2','image_main3','image_main4','image_main5']})
    ]

    # name 필드 명 수정
    def title(self, title):
        return title.name
    title.short_description = "상품명"

    # 메인 이미지 URL 출력 설정
    def image_tag(self, obj):
        if obj.image_main:
            for i in obj.image_main[0]:
                return mark_safe('<img src={} style = "width: 50px;"/>'.format(obj.image_main.url))
        return None
    image_tag.short_description = "메인 사진"

    # quantity 필드명 수정
    def cnt_q(self, qu):
        return intcomma(qu.quantity)
    cnt_q.short_description = "재고 량"

    # 가격 천 단위 구분을 출력
    def comma_price(self, pay):
        return intcomma(pay.price)
    comma_price.short_description = "가격(원)"

    # Product 검색 기능 추가
    search_fields = ['name', 'serial', 'category']

admin.site.register(Products, InfoProductAdmin)