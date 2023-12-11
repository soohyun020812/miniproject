# def dictfetchall(cursor):
#     # (1, '제목1', '작성자1', <cx_Oracle.LOB object at 0x0000025781A68C60>, datetime.datetime(2023, 5, 19, 14, 16, 42), 0) 여기서 제목만 가져오게싿...이말임.

#     columns= [ col[0].lower() for col in cursor.description]
#     #cursor의 description에 각 필드 이름 정보 - 배열
#     #columns['id', 'title','contents','writer']
    
#     return [dict(zip(columns,row)) for row in cursor.fetchall()]
#     #{'id':1,'title':'제목1', .....} 로 만들려는 것


#     # dict로 바꿔주는 이유: tuple는 indexing으로만 접근도니다

def dictfetchall(cursor):
    """
    [('ID', <cx_Oracle.DbType DB_TYPE_NUMBER>, 20, None, 19, 0, 0), ('TITLE', <cx_Oracle.DbType DB_TYPE_NVARCHAR>, 100, 400, None, None, 1), ('WRITER', <cx_Oracle.DbType DB_TYPE_NVARCHAR>, 100, 400, None, None, 1), ('CONTENTS', <cx_Oracle.DbType DB_TYPE_NCLOB>, None, None, None, None, 1), ('WDATE', <cx_Oracle.DbType DB_TYPE_TIMESTAMP>, 23, None, 0, 6, 0), ('HIT', <cx_Oracle.DbType DB_TYPE_NUMBER>, 12, None, 11, 0, 0)]
    """
    #print( cursor.description )
   
    
    #cursor의  description에 각 필드 이름 정보 - 배열 
    #colums ['id', 'title', 'contents', 'writer']
    #[1, '제목1', '내용1', '작성자1']
    #{'id':1, 'title':'제목1' , .....}
    columns = [ col[0].lower() for col in cursor.description]
    #print( columns  )
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

    """
    [(1, "제목1', '내용1')
    cursor.description
    [{"id":1, "title":"제목1"}]
    """

    #<< < 1 2 3 4 5 6 7 8 9 10 > >>
    #<<: 첫 번째 페이지, 항상
    #< : 현재 페이지로부터 앞으로 이동할 페이지가 있는지 
    #현재 9페이지: 이전 < 8페이지
    # 1,2,3 ... 10 첫번째 그룹: 1~10    현재:4      1번 그룹
    #               두번째 그룹: 11~20      :12     2번 그룹   
    #               세번째 그룹: 21~30      :29     3번 그룹
    #>: 현재 페이지로부터 뒤로 이동할 페이지가 있는지 현재 9 다음> 10페이지
    #>>: 마지막 페이지

import math
class CommonPage:
    #페이징에 필요한 3가지 정보(전체개수, 한페이지에 표시될 개수, 현재 페이지)
    #totalCnt: 전체 데이터 개수 
    #pageSize: 한페이지에 데이터를 몇 건씩 보여줄거야
    #전체 페이지 개수: ceil(totalCnt/pageSize)        
    # 232/10 - 23.2 - 올림(무조건) - 24페이지
    #curPage: 현재 페이지
    #파이썬에 클래스 설계할 때 가급적 생성자에서 변수를 만드는게 낫다. 
    def __init__(self, totalCnt=1, curpage=0, pageSize=10):
        self.curPage=curpage
        self.totalCnt=totalCnt
        self.totalPage=math.ceil(totalCnt/pageSize)-1
        self.start=(self.curPage//pageSize)*10 #그룹 시작
        self.end=self.start+10
        if self.end>self.totalPage:
            self.end=self.totalPage+1
        # pass 이럴 때 써먹는 거임. 일단 나중에 더 추가하려는 거임.

        #3  1   10
        #12 11  2
        #32 30  40

        if self.curPage>=1:
            self.isPrev=True
            self.prev_page=self.curPage-1
        else:   #더이상 앞으로 갈 수 없음
            self.isPrev=False
            self.prev_page=0
        
        if self.curPage<=self.totalPage:
            self.isNext=True
            self.next_page=self.curPage+1
        else:   #더이상 앞으로 갈 수 없음
            self.isNext=False
            self.next_page=self.curPage


        self.page_range= range(self.start,self.end)
        