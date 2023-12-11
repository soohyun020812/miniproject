from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .CommonUtil import dictfetchall, CommonPage 


def index(request):
    return HttpResponse("<h1>Person</h1>")

# def index(request):
    # return render(request, 'service/choosebar.html')

def show_map(request):
    return render(request, 'service/map.html')

import csv
from service.models import MyModel
from service.forms import MyForm


from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection
from django.http import JsonResponse, HttpResponse
import json 

#sql에서 받아오기
def custom_sql_query(request):
    # lat=request.GET.get("Ma")
    # lon=request.GET.get("La")
    # print(lon)
    params = request.GET
    
# 특정 키의 값 가져오기
    lat = params.get("Ma")
    lon = params.get("La")
    sql=f"""
    select * from 
    (
    select  상권업종중분류명, count(*)  cnt 
    from 
    (
        select A.*
        from
        (
            SELECT 
                    상권업종중분류명, 
                    위도, 
                    경도,
                    (6371000 * ACOS(COS({lat}/57.29577951) * COS(TO_NUMBER(위도)/57.29577951) * COS(TO_NUMBER(경도)/57.29577951 - {lon}/57.29577951) + SIN({lat}/57.29577951) * SIN(TO_NUMBER(위도)/57.29577951))) as 거리
            from MARKETFINAL0527
        )A
        where 거리<300
    )A
    group by A.상권업종중분류명
    order by cnt desc
    )
    where rownum <=3
    """

    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = dictfetchall(cursor)
        jsonStr = json.dumps(rows, ensure_ascii=False).encode('utf8')
        print(rows)
    # # Fetch the column names from the cursor ""description
    #     col_names = [desc[0] for desc in cursor.description]


        return HttpResponse(jsonStr, content_type="application/json;charset=utf-8")





# from service.forms import MyForm

# html에서 받아온 사용자 값을 모델에 저장하기 (우리의 데이터)
def save(request):
    data = request.POST.get('searchInput')
    # form 객체 다 들고옴 ; 클라이언트로 부터 전달된 데이터인 form 객체를 생성 
    # if data.is_valid():
        # result = form.sav/e(commit=True)  # 디비에 알아서 저장된다. Insert쿼리 자동생성ㅇ
    return HttpResponse(data)
    

# csv파일을 불러와서 모델에 저장하기 (보여줄 데이터)

def save_data_to_model(request):
    csv_file = settings.DATA_CSV_URL
    with open(csv_file, 'r', newline='') as file:  # file 변수에 할당하여 읽기위함
        reader = csv.DictReader(file)  # csv파일을 읽음 
        for row in reader:
            MyModel.objects.create(
                store_name = row['상호명'],
                store_code = row['상권업종중분류코드'],
                store_segment=row['상권업종중분류명'],
                address_dong=row['법정동명'],
                address_road=row['도로명'],
                longitude=float(row['경도']),
                latitude=float(row['위도'])
            )
        # form_object = my_form.save(commit=True)   # 저장된 데이터의 모든 필드값을 갖는다. 
    # return redirect(form_object)


def write(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # 폼이 유효한 경우, 필요한 처리를 수행
            # ...
            return redirect("index")  # 처리가 완료된 후에는 다시 index로 이동
    else:
        form = MyForm()

    context = {"form": MyForm(request.POST)}
    return render(request, "service/index.html", context)


def generate_report(request):
    # 특정 영역의 경도, 위도 범위를 설정합니다.
    min_longitude = 127.0
    max_longitude = 128.0
    min_latitude = 37.0
    max_latitude = 38.0

    # 특정 영역 내에 있는 상권 정보를 조회합니다.
    model_result = MyModel.objects.filter(
        longitude__gte=min_longitude,
        longitude__lte=max_longitude,
        latitude__gte=min_latitude,
        latitude__lte=max_latitude
    )

    # 조회된 상권 정보를 리포트로 보여줍니다.
    context = {'model_result': model_result}
    return render(request, "service/report.html", context)


from django.shortcuts import render, redirect
from .forms import UserInputForm


# 사용자 입력값 받기 
def user_input_view(request):   
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()  # 입력 값을 데이터베이스에 저장
            return redirect('success')  # 저장 후 리다이렉션할 URL
    else:
        form = UserInputForm()
    return render(request, 'index.html', {'form': form})


from service.forms import SignupForm 
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()  # 데이터 저장
            return redirect('success_page')
    else:
        form = SignupForm()
    return render(request, 'service/signup.html', {'form': form})

def login(request) :
    if request.method == "POST" :
        pass
    else :
        return render(request, "service/login.html")