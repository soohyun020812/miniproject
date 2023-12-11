from django.shortcuts import render
from board.models import Board #Board모델을 import 하고 
from board.forms import BoardForm
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import redirect 
from django.db import connection 
from service.CommonUtil import dictfetchall, CommonPage
from django.http import JsonResponse  
import json 
from .models import Board

def list(request):
    boardList = Board.objects.all()
    boardList = Board.objects.order_by('-id')
    return render(request, "board/board_list.html", {'boardList':boardList} )


def list2(request, pg):
    cursor = connection.cursor() 
    sql = "select count(*) from board_board "
    cursor.execute(sql)
    totalCnt = int(cursor.fetchone()[0])   
    cp = CommonPage(totalCnt, pg, 10)
    sql = f"""
        select A.id, A.title, A.writer, A.contents, 
            to_char(A.wdate, 'yyyy-mm-dd') wdate, hit, num
        from
        (
            select id, title, writer, contents, wdate, hit,
            row_number() over(order by id desc) num,
            ceil(row_number() over(order by id desc)/10)-1 pg 
            from board_board    -- 검색 조건 필요할 경우에 여기에 
        )A
        where A.pg={pg}
    """
    cursor.execute(sql)

    boardList = dictfetchall(cursor)
    # print(cp.totalPage)
    return render(request, "board/board_list.html", {'boardList':boardList,"commonPage":cp} )

def views(request, id):
    board = Board.objects.get(id=id)
    board.hit = board.hit+1  
    return render(request, "board/board_view.html", {'boardItem':board})




def write(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False) 
            board.save()  
            return JsonResponse({"message": "글이 성공적으로 저장되었습니다."}, status=200)
        else:
            return JsonResponse({"message": "글 저장에 실패했습니다. 다시 시도해주세요."}, status=400)

    else:
        form = BoardForm()

    context = {"form": form}
    return render(request, "board/board_write.html", context)

# def write(request):
#     if request.method == "POST":
#         form = BoardForm(request.POST)
#         if form.is_valid():
#             board = form.save(commit=False) 
#             board.save()  
#             return HttpResponse("글이 성공적으로 저장되었습니다.")
#     else:
#         form = BoardForm()

#     context = {"form": form}
#     return render(request, "board/board_write.html", context)



def save(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False) 
            board.wdate = timezone.now()
            board.hit = 0
            board.save()
            return JsonResponse({"message": "글이 성공적으로 저장되었습니다."}, status=200)
        else:
            return JsonResponse({"message": "글 저장에 실패했습니다. 다시 시도해주세요."}, status=400)
    return JsonResponse({"message": "잘못된 요청입니다."}, status=400)

# def save(request):
#     form = BoardForm(request.POST)
#     board = form.save(commit=False) 
#     board.wdate =  timezone.now()  #현재 시간 저장
#     board.hit=0
#     board.save()
#     return redirect("board:list", pg=0)




def modify(request):
    #jsonObject = json.loads(request.body)
    result = {"result":"success", "title":"title", 
              "writer":"author"}
    return JsonResponse(result, status=200) 


from django.db.models import Count
from django.shortcuts import render
from .models import Board

def write_datas(request, category):
    count = Board.objects.filter(category=category).count()

    context = {
        'category': category,
        'count': count
    }

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# from .models import CheckedValues

# 점포 유형 카운트 세는 로직 
@csrf_exempt
def save_checked_values(request):
    if request.method == "POST":
        checked_values = request.POST.getlist("checkedValues[]")
        print(checked_values)
        # 예를 들어, CheckedValues 모델에 저장한다고 가정하면:
        # for value in checked_values:
            # checked_value, created = CheckedValues.objects.get_or_create(value=value)
            # checked_value.count += 1
            # checked_value.save()

        # return JsonResponse({"message": "선택된 카운트가 저장되었습니다."})

    # return JsonResponse({"message": "잘못된 요청입니다."})
