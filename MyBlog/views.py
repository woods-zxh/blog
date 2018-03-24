#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from .models import superuser
from django.utils import timezone
from django.http import HttpResponse
import datetime
# from uuslug import slugify
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


#注册
def regist(request):
    if request.method == 'POST':
            #获得表单数据
        username =request.POST['username']
        user = superuser.objects.filter(username__exact=username)
        if user:
            return render_to_response('Register2.html', )
        else:
            password = request.POST['password']
            cha = request.POST.get('cha')
            touxiang = request.FILES.get('touxiang',"")
            superuser.objects.create_user(username=username, password=password, cha=cha, touxiang=touxiang)

            user = authenticate(username=username, password=password)
            print(user.username)
            response = HttpResponseRedirect('/online/')
            # response.set_cookie('username', username, 3600)
            return response

    else:
        return render_to_response('Register.html', )
#登陆

def login1(request):
    if request.method == 'POST':
            #获取表单用户密码
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password=password)

        if user is not None:
            login(request, user)
             #比较成功，跳转index
            response = HttpResponseRedirect('/online/index/')
                #将username写入浏览器cookie,失效时间为3600
            # response.set_cookie('username',username,3600)
            return response
        else:
                #比较失败，还在login
            # return HttpResponseRedirect('/online/login/')
            return render_to_response('Login.html')
    else:
         return render_to_response('Login2.html')
#登陆成功

def index(request):
    user = request.user
    times = user.sighs
    cha = user.cha
    username = user.username
    touxiang = user.touxiang
    latest_diary_list = user.diary_set.order_by('-pub_date')[:3]
    latest_img_list = user.img_set.order_by('-pub_date')[:3]
    return render_to_response('mainbody3.html', {"username": username, "times": times, "cha": cha,"touxiang":touxiang,
                                                 "latest_diary_list": latest_diary_list,"latest_img_list":latest_img_list})
#分类
def show1(req):
    user = req.user
    message = user.diary_set.order_by('-pub_date')[:100]
    lastest_diary_list = []
    for x in message:
        if x.kind == "音乐类":
            lastest_diary_list.append(x)
    return render_to_response('memory1.html',{"username":  user.username, "user": user, "latest_diary_list": lastest_diary_list})


def show2(req):
    user = req.user
    message = user.diary_set.order_by('-pub_date')[:100]
    lastest_diary_list = []
    for x in message:
        if x.kind == "学习类":
            lastest_diary_list.append(x)
    return render_to_response('memory2.html',{"username": user.username,"user":user,"latest_diary_list":lastest_diary_list})

def show3(req):
    user = req.user
    message = user.diary_set.order_by('-pub_date')[:100]
    lastest_diary_list = []
    for x in message:
        if x.kind == "人际交往类":
            lastest_diary_list.append(x)
    return render_to_response('memory3.html',{"username":  user.username, "user": user, "latest_diary_list": lastest_diary_list})


def show4(req):
    user = req.user
    message = user.diary_set.order_by('-pub_date')[:100]
    lastest_diary_list = []
    for x in message:
        if x.kind == "其他类":
            lastest_diary_list.append(x)
    return render_to_response('memory4.html',{"username":  user.username, "user": user, "latest_diary_list": lastest_diary_list})

#上传表单
def write(request):
    user = request.user
    if request.method == 'POST':
        content = request.POST["a"]
        title = request.POST["title"]
        radio = request.POST["type"]
        diary1 = user.diary_set.filter(title = title)
        if diary1:
            return HttpResponse("该标题已存在")
        else:
            user.diary_set.create(diary_txt=content, pub_date=timezone.now(), kind=radio, title=title)
        if request.FILES.get("img"):
            user.img_set.create(img=request.FILES['img'], pub_date=timezone.now())
            response = HttpResponseRedirect('/online/index/')
            return response

        else:
            response = HttpResponseRedirect('/online/index/')
            return response

    else:
        return render_to_response('write.html')

#删除
def delete(request):
    user = request.user
    id = request.POST["id"]
    type = request.POST["type"]
    loser = user.diary_set.get(id=id)
    loser.delete()
    if  type == "1" :
        response = HttpResponseRedirect('/online/show1/')
    elif type == "2" :
        response = HttpResponseRedirect('/online/show2/')
    elif type == "3":
        response = HttpResponseRedirect('/online/show3/')
    else:
        response = HttpResponseRedirect('/online/show4/')
    return response
#修改
def change(request):
    user = request.user
    type = request.POST["type"]
    content = request.POST["a"]
    id = request.POST['id']
    loser = user.diary_set.get(id=id)
    loser.diary_txt = content
    loser.save()
    if   type == "1":
        response = HttpResponseRedirect('/online/show1/')
    elif type == "2":
        response = HttpResponseRedirect('/online/show2/')
    elif type == "3":
        response = HttpResponseRedirect('/online/show3/')
    else:
        response = HttpResponseRedirect('/online/show4/')
    return response
#评论
def comment(request):
    user = request.user
    type = request.POST["type"]
    content = request.POST["a"]
    id = request.POST['id']
    loser = user.diary_set.get(id=id)
    loser.comment_set.create(comment=content, )
    if   type == "1":
        response = HttpResponseRedirect('/online/show1/')
    elif type == "2":
        response = HttpResponseRedirect('/online/show2/')
    elif type == "3":
        response = HttpResponseRedirect('/online/show3/')
    else:
        response = HttpResponseRedirect('/online/show4/')
    return response
#搜索
def search(request):
    user = request.user
    keyword= request.POST["key"]
    message = user.diary_set.all()
    SearchResult = []
    for x in message:
        if keyword in x.diary_txt:
            SearchResult.append(x)
    ResultAmount = len(SearchResult)

    return render(request, 'memory5.html', {  "SearchResult": SearchResult,"ResultAmount": ResultAmount})
#详情（为了使用slugfeild,特意弄的）
def detail(request, slug):
    user = request.user
    loser = user.diary_set.get(slug = slug)
    a = loser
    return render_to_response('memory6.html',{"username": user.username,"user":user,"a":a})
#登出
def logout(req):
    response = HttpResponseRedirect('/online')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response
#上传图片
def uploadImg(request):
    user = request.user
    if request.method =='POST':
        if request.FILES.get("img"):
            user.img_set.create(img = request.FILES['img'],pub_date = timezone.now())
            return HttpResponse("1")

        else:
            return render(request, 'mainbody3.html')

    else:
        return render(request,'uploadimg.html')
#展示图片
def showImg(request):
    user = request.user
    latest_img_list = user.img_set.order_by('-pub_date')[:10]
    content = {
        'latest_img_list':latest_img_list,
    }
    return render_to_response('memory0.html',content)

#签到
def sigh(request):
    user = request.user
    if user.date==datetime.datetime.now().day:
        times = user.sighs
        cha = user.cha
        latest_diary_list = user.diary_set.order_by('-pub_date')[:3]
        latest_img_list = user.img_set.order_by('-pub_date')[:3]

        content = {"username": user.username, "times": times, "cha": cha,
                   "latest_diary_list": latest_diary_list,
                   'latest_img_list': latest_img_list}
        return render_to_response('mainbody3.html', content)
    else:
        user.date = datetime.datetime.now().day
        user.sighs += 1
        user.save()
        times = user.sighs
        cha = user.cha
        latest_diary_list = user.diary_set.order_by('-pub_date')[:3]
        latest_img_list = user.img_set.order_by('-pub_date')[:3]

        content = {"username":  user.username, "times": times, "cha": cha,
                   "latest_diary_list": latest_diary_list,
                   'latest_img_list': latest_img_list}
        return render_to_response('mainbody3.html',content)
