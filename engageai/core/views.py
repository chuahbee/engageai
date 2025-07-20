from django.shortcuts import render
from core.kmp import kmp_search
from interaction.models import KMPInteraction
from core.openai_helper import get_ai_response

KEYWORDS = ["支付失败", "API问题", "没有客服", "电商网站", "需要帮助"]

print("✅ 准备保存记录")

def keyword_match_view(request):
    result = ""
    if request.method == 'POST':
        text = request.POST.get('text')
        print("用户输入：", text)  # ✅ 调试输出
        matched = ""
        response_text = ""

        if text:
            for kw in KEYWORDS:
                if kmp_search(text, kw):
                    matched = kw
                    result = f"识别关键词：{kw}，建议回复：我们可以协助处理“{kw}”的问题。"
                    break

            if not result:
                result = "未匹配任何关键词，请转人工客服。"
                matched = None
                response_text = get_ai_response(text)
            else:
                response_text = result  # 也可以使用 get_ai_response(text)

            print("✅ 准备保存记录")  # 加这一行确认是否进入这里

            KMPInteraction.objects.create(
                input_text=text,
                matched_keyword=matched,
                response_text=response_text
            )
        else:
            result = "请输入内容再提交。"

    return render(request, 'core/kmp_test.html', {'result': result})
