from django.shortcuts import render
from calendarSite.forms import addDataForm
from calendarSite.forms import indexForm
# from calendarSite.forms import searchForm
from calendarSite.forms import subjectForm
from calendarSite.forms import userForm

# Create your views here.


def index(request):
    return render(request, 'index.html')

def search(request):
   if request.POST:
      # form = searchForm(request.POST or None)
      subject = request.POST.getlist("subject") 
      print(subject)

   # メッセージ情報を取得。ない場合は空文字が入る
   
   """if  subject != '':
        # メッセージの内容をDBに登録
        CalendarModel = Calendar(subject=subject)
        CalendarModel.save()

    CalendarList = Calendar.objects.all()

    return render(request, 'search.html',{
        "CalendarList": CalendarList
    })

    dbData = {
        "id": 123,
        "name": "name",
        "form": form,
        "CalendarList" : CalendarList,
    }"""
   return render(request, 'user.html')

def addData(request):
   date=0
   user='かいた'
   subject='おーいお茶'
   title='伊藤園'
   caleList=[{
      'id':'',
      'title':'ワクチン',
      'date':'2021-09-03',
      'user':'',
   }]

   form=addDataForm(request.POST or None)

   date=form['date'].data or ''
   user=form['user'].data or ''
   subject=form['subject'].data or ''
   title=form['title'].data or ''

   caleList[0]['date']=date  
   caleList[0]['title']=title  
   #print(form)

   print(str(date))
   print(str(user))
   print(str(subject))
   print(str(title))
   print(caleList)

   if date!=''and user!='' and subject!='' and title!='':
      return render(request,'user.html',{
         "caleList":caleList,
         "date":date,
         "title":title
      })
   return render(request, 'addData.html')

def user(request):
   return render(request, 'user.html')

def subject(request):
   return render(request, 'subject.html')

