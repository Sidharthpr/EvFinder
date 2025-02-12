from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('login', views.login, name='login'),
path('index', views.index, name='index'),
path('register', views.register, name='register'),
path('loginhandler', views.loginhandler, name='loginhandler'),
path('registerhandler', views.registerhandler, name='registerhandler'),
path('updateprofile', views.updateprofile, name='updateprofile'),
path('userhome', views.userhome, name='userhome'),
path('updateuserprofilehandler', views.updateuserprofilehandler, name='updateuserprofilehandler'),
path('viewuserprofile', views.viewuserprofile, name='viewuserprofile'),
path('postfeedback',views.postfeedback,name='postfeedback'),
path('feedbackhandler',views.feedbackhandler,name='feedbackhandler'),
path('viewfeedback',views.viewfeedback,name='viewfeedback'),
path('allstation',views.allstation,name='allstation'),
path('adminlogin', views.adminlogin, name='adminlogin'),
path('adminloginhandler', views.adminloginhandler, name='adminloginhandler'),
path('adminhome', views.adminhome, name='adminhome'),




path('addstation', views.addstation, name='addstation'),
path('addstationhandler', views.addstationhandler, name='addstationhandler'),
# path('updatestation', views.updatestation, name='updatestation'),
path('adminhome', views.adminhome, name='adminhome'),
# path('updatestationhandler', views.updatestationhandler, name='updatestationhandler'),
# path('search', views.search, name='search'),
path('searchhandler', views.searchhandler, name='searchhandler'),
# path('bookedhandler', views.bookedhandler, name='bookedhandler'),
path('adminviewallstation',views.adminviewallstation,name='adminviewallstation'),
path('adminviewuser', views.adminviewuser, name='adminviewuser'),
path('adminreplayhandler',views.adminreplayhandler,name='adminreplayhandler'),
path('adminviewfeedback',views.adminviewfeedback,name='adminviewfeedback'),
path('adminviewrequst',views.adminviewrequst,name='adminviewrequst'),
path('bookapprovehandler',views.bookapprovehandler,name='bookapprovehandler'),

path('deletehandler',views.deletehandler,name='deletehandler'),
path('confirm',views.confirm,name='confirm'),
path('adminapproverequst',views.adminapproverequst,name='adminapproverequst'),
path('confirmhandler',views.confirmhandler,name='confirmhandler'),

# path('sbookedhandler', views.sbookedhandler, name='sbookedhandler'),
path('bookedpay', views.bookedpay, name='bookedpay'),
path('payhandler', views.payhandler, name='payhandler'),
path('deleteuserhandler', views.deleteuserhandler, name='deleteuserhandler'),
path('deletestationhandler', views.deletestationhandler, name='deletestationhandler'),
path('deleterequesthandler', views.deleterequesthandler, name='deleterequesthandler'),

path('deletefeedbackhandler',views.deletefeedbackhandler,name='deletefeedbackhandler'),
path('adminviewusing',views.adminviewusing,name='adminviewusing'),
path('recivehandler',views.recivehandler,name='recivehandler'),
path('usinghandler',views.usinghandler,name='usinghandler'),
path('finishhandler',views.finishhandler,name='finishhandler'),
path('booked',views.booked,name='booked'),
path('finalbookhandler',views.finalbookhandler,name='finalbookhandler'),
path('cancelhandler',views.cancelhandler,name='cancelhandler'),
path('delete',views.delete,name='delete'),
path('deletebookhandler',views.deletebookhandler,name='deletebookhandler'),

path('deletedhandler',views.deletedhandler,name='deletedhandler'),



]
