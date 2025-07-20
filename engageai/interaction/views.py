from django.shortcuts import render
from .models import KMPInteraction

# Create your views here.
KEYWORD_RESPONSES = {
    '退款': '您可以在订单页面申请退款。',
    '发货': '商品将在24小时内发货。',
    '客服': '请拨打客服电话 12345678。',
    '账号': '请提供您的账号信息以便查询。',
}

def kmp_test(request):
    response_text = ''
    matched_keyword = ''
    
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')

        # 匹配关键词
        for keyword, reply in KEYWORD_RESPONSES.items():
            if keyword in input_text:
                matched_keyword = keyword
                response_text = reply
                break
        else:
            response_text = '未匹配任何关键词，请转人工客服。'

        # 保存到数据库
        KMPInteraction.objects.create(
            input_text=input_text,
            matched_keyword=matched_keyword or None,
            response_text=response_text
        )

    return render(request, 'core/kmp_test.html', {
        'response': response_text
    })