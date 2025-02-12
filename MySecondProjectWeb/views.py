from django.shortcuts import render, redirect
from django.utils import timezone
from .models import UserDetail, Feedback, Station, UserBookRequest

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def loginhandler(request):
    username = request.GET.get("un")
    password = request.GET.get("pw")
    
    try:
        user = UserDetail.objects.get(uusername=username, upassword=password)
        request.session['sname'] = user.uname
        request.session['sno'] = user.uno
        return render(request, 'userhome.html', {'dname': request.session['sname']})
    except UserDetail.DoesNotExist:
        return render(request, 'login.html', {'dmsg': 'Invalid Username/Password'})

def registerhandler(request):
    UserDetail.objects.create(
        uname=request.GET.get("n"),
        vehicle=request.GET.get("v"),
        udob=request.GET.get("d"),
        uphone=request.GET.get("p"),
        uemail=request.GET.get("e"),
        uusername=request.GET.get("uname"),
        upassword=request.GET.get("ps")
    )
    return register(request)

def updateprofile(request):
    user = UserDetail.objects.get(uno=request.session['sno'])
    return render(request, 'updateprofile.html', {'drow': user})

def userhome(request):
    return render(request, 'userhome.html', {'dname': request.session['sname']})

def updateuserprofilehandler(request):
    user = UserDetail.objects.get(uno=request.session['sno'])
    user.vehicle = request.GET.get("v")
    user.uemail = request.GET.get("e")
    user.uphone = request.GET.get("p")
    user.upassword = request.GET.get("ps")
    user.save()
    return updateprofile(request)

def viewuserprofile(request):
    user = UserDetail.objects.get(uno=request.session['sno'])
    return render(request, 'viewprofile.html', {
        'dname': request.session['sname'],
        'drow': user
    })

def postfeedback(request):
    return render(request, 'postfeedback.html')

def feedbackhandler(request):
    Feedback.objects.create(
        userid=request.session['sno'],
        username=request.session['sname'],
        usertype='user',
        feedback=request.GET.get("f"),
        details=request.GET.get("ta"),
        date=timezone.now().strftime("%b-%d-%y"),
        remark=''
    )
    return postfeedback(request)

def viewfeedback(request):
    feedbacks = Feedback.objects.filter(userid=request.session['sno'])
    return render(request, 'viewfeedback.html', {
        'dname': request.session['sname'],
        'drow': feedbacks
    })

def allstation(request):
    stations = Station.objects.all()
    return render(request, 'allstation.html', {
        'dname': request.session['sname'],
        'drow': stations
    })

def adminlogin(request):
    return render(request, 'adminlogin.html')

def adminloginhandler(request):
    username = request.GET.get("un")
    password = request.GET.get("pw")
    
    if username == "admin" and password == "admin":
        return render(request, 'adminhome.html')
    return render(request, 'adminlogin.html')

def addstation(request):
    return render(request, 'addstation.html')

def addstationhandler(request):
    evsname = request.GET.get("e")
    Station.objects.create(
        admin='admin',
        distric=request.GET.get("d"),
        city=request.GET.get("c"),
        evsname=evsname,
        price=request.GET.get("p"),
        videolink=f"https://meet.jit.si/evfinder{evsname}"
    )
    return addstation(request)

# Continue with similar pattern for other views...
# I'll show a few more key examples:

def searchhandler(request):
    stations = Station.objects.filter(distric__icontains=request.GET.get("sr"))
    return render(request, 'search.html', {
        'dname': request.session['sname'],
        'drow': stations
    })

def bookapprovehandler(request):
    booking = UserBookRequest.objects.get(rid=request.GET.get("approvedid"))
    booking.status = 'approved'
    booking.save()
    return adminviewrequst(request)

def finishhandler(request):
    booking_id = request.GET.get("finishid")
    station_id = request.GET.get("stationsid")
    
    # Update booking status
    booking = UserBookRequest.objects.get(rid=booking_id)
    booking.status = 'complete'
    booking.save()
    
    # Update station status
    station = Station.objects.get(sid=station_id)
    station.bookstatus = 'available'
    station.save()
    
    return confirm(request)

def adminviewallstation(request):
    stations = Station.objects.all()
    return render(request, 'adminviewallstation.html', {'drow': stations})

def adminviewuser(request):
    users = UserDetail.objects.all()
    return render(request, 'adminviewuser.html', {'drows': users})

def adminhome(request):
    return render(request,'adminhome.html')

def adminviewfeedback(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'adminviewfeedback.html', {'drow': feedbacks})

def adminreplayhandler(request):
    feedback = Feedback.objects.get(fid=request.GET.get("id"))
    feedback.remark = request.GET.get("replay")
    feedback.save()
    return adminviewfeedback(request)

def adminviewrequst(request):
    requests = UserBookRequest.objects.filter(status='created')
    return render(request, 'adminviewrequst.html', {'drow': requests})

def bookapprovehandler(request):
    booking = UserBookRequest.objects.get(rid=request.GET.get("approvedid"))
    booking.status = 'approved'
    booking.save()
    return adminviewrequst(request)

def deletehandler(request):
    UserBookRequest.objects.filter(rid=request.GET.get("selectid")).delete()
    return adminviewrequst(request)

def confirm(request):
    requests = UserBookRequest.objects.filter(uname=request.session['sname'])
    return render(request, 'confirm.html', {'drow': requests})

def adminapproverequst(request):
    requests = UserBookRequest.objects.filter(status='approved')
    return render(request, 'adminapproverequst.html', {'drow': requests})

def confirmhandler(request):
    booking = UserBookRequest.objects.get(rid=request.GET.get("id"))
    return render(request, 'bookedpay.html', {'drow': booking})

def bookedpay(request):
    booking = UserBookRequest.objects.first()
    return render(request, 'bookedpay.html', {'drow': booking})

def payhandler(request):
    booking = UserBookRequest.objects.get(rid=request.GET.get("rid"))
    booking.bookedremark = 'recived'
    booking.save()
    return bookedpay(request)

def deleteuserhandler(request):
    UserDetail.objects.filter(uno=request.GET.get("selectedid")).delete()
    return adminviewuser(request)

def deletestationhandler(request):
    Station.objects.filter(sid=request.GET.get("selectedid")).delete()
    return adminviewallstation(request)

def deleterequesthandler(request):
    UserBookRequest.objects.filter(rid=request.GET.get("selectedid")).delete()
    return adminapproverequst(request)

def deletefeedbackhandler(request):
    Feedback.objects.filter(fid=request.GET.get("selectid")).delete()
    return viewfeedback(request)

def adminviewusing(request):
    requests = UserBookRequest.objects.exclude(status='cancelled')
    return render(request, 'adminviewusing.html', {'drow': requests})

def recivehandler(request):
    booking = UserBookRequest.objects.get(rid=request.GET.get("reciveid"))
    booking.status = 'recived'
    booking.save()
    return confirm(request)

def usinghandler(request):
    booking = UserBookRequest.objects.get(rid=request.GET.get("useid"))
    booking.status = 'using'
    booking.save()
    return confirm(request)

def finishhandler(request):
    booking = UserBookRequest.objects.get(rid=request.GET.get("finishid"))
    booking.status = 'complete'
    booking.save()
    
    station = Station.objects.get(sid=request.GET.get("stationsid"))
    station.bookstatus = 'available'
    station.save()
    return confirm(request)

def booked(request):
    latest_booking = UserBookRequest.objects.last()
    return render(request, 'booked.html', {
        'dname': request.session['sname'],
        'drow': latest_booking
    })

def finalbookhandler(request):
    station = Station.objects.get(sid=request.GET.get("confirmid"))
    station.bookstatus = 'Not Available'
    station.save()
    return allstation(request)

def cancelhandler(request):
    station = Station.objects.get(sid=request.GET.get("cancelid"))
    station.bookstatus = 'available'
    station.save()
    return delete(request)

def delete(request):
    stations = Station.objects.all()
    return render(request, 'delete.html', {'drow': stations})

def cancellhandler(request):
    station = Station.objects.get(sid=request.GET.get("cancelid"))
    station.bookstatus = 'available'
    station.save()
    return confirm(request)

def deletebookhandler(request):
    UserBookRequest.objects.filter(rid=request.GET.get("selectedid")).delete()
    return allstation(request)

def deletedhandler(request):
    booking = UserBookRequest.objects.get(rid=request.GET.get("selectedid"))
    booking.status = 'cancelled'
    booking.save()
    
    station = Station.objects.get(sid=request.GET.get("stationid"))
    station.bookstatus = 'available'
    station.save()
    return confirm(request)

# def sbookedhandler(request):
#     """
#     Handles marking a station as booked (for example, by a station manager).
#     Expects a POST request with a 'station_id'.
#     """
#     if request.method == "POST":
#         station_id = request.POST.get("station_id")
#         try:
#             station = Station.objects.get(sid=station_id)
#             station.bookstatus = "Not Available"
#             station.save()
#             return JsonResponse({
#                 "status": "success",
#                 "message": "Station marked as booked."
#             })
#         except Station.DoesNotExist:
#             return JsonResponse({
#                 "status": "error",
#                 "message": "Station not found."
#             })
#     return HttpResponse("Method Not Allowed", status=405)

# def bookedhandler(request):
#     """
#     Handles a user booking request.
#     Expects a POST request with the station ID and user name.
#     """
#     if request.method == "POST":
#         station_id = request.POST.get("station_id")
#         uname = request.POST.get("uname")
#         try:
#             station = Station.objects.get(sid=station_id)
#             # Create a booking record using details from the station
#             booking = UserBookRequest.objects.create(
#                 uname=uname,
#                 distric=station.distric,
#                 city=station.city,
#                 evsname=station.evsname,
#                 price=station.price,
#                 station=station
#             )
#             return JsonResponse({
#                 "status": "success",
#                 "message": "Booking request created.",
#                 "booking_id": booking.rid
#             })
#         except Station.DoesNotExist:
#             return JsonResponse({
#                 "status": "error",
#                 "message": "Station not found."
#             })
#     return HttpResponse("Method Not Allowed", status=405)

# def updatestation(request):
#     """
#     Displays a form to update a station's details.
#     Expects a GET parameter 'sid' (station ID).
#     """
#     station_id = request.GET.get("sid")
#     try:
#         station = Station.objects.get(sid=station_id)
#         return render(request, "updatestation.html", {"station": station})
#     except Station.DoesNotExist:
#         return HttpResponse("Station not found.", status=404)

# def updatestationhandler(request):
#     """
#     Processes the station update form.
#     Expects a POST request with updated station details.
#     """
#     if request.method == "POST":
#         station_id = request.POST.get("sid")
#         try:
#             station = Station.objects.get(sid=station_id)
#             station.evsname = request.POST.get("evsname", station.evsname)
#             station.distric = request.POST.get("distric", station.distric)
#             station.city = request.POST.get("city", station.city)
#             station.price = request.POST.get("price", station.price)
#             station.videolink = request.POST.get("videolink", station.videolink)
#             station.save()
#             # Redirect to a page that shows all stations (adjust the URL name as needed)
#             return redirect("adminviewallstation")
#         except Station.DoesNotExist:
#             return HttpResponse("Station not found.", status=404)
#     return HttpResponse("Method Not Allowed", status=405)

# def search(request):
#     """
#     Searches for stations based on a district query.
#     Expects a GET parameter 'sr' containing the search term.
#     """
#     query = request.GET.get("sr", "")
#     stations = Station.objects.filter(distric__icontains=query)
#     return render(request, "search.html", {
#         "dname": request.session.get("sname", ""),
#         "drow": stations
#     })