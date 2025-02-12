from django.db import models

class Feedback(models.Model):
    fid = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    usertype = models.CharField(max_length=30)
    feedback = models.CharField(max_length=30)
    details = models.CharField(max_length=30)
    remark = models.CharField(max_length=20)
    date = models.CharField(max_length=20)

    class Meta:
        db_table = 'feedbacks'

class Station(models.Model):
    sid = models.AutoField(primary_key=True)
    admin = models.CharField(max_length=30)
    distric = models.CharField(max_length=30)  # Original spelling maintained
    city = models.CharField(max_length=30)
    evsname = models.CharField(max_length=30)
    price = models.CharField(max_length=20)
    bookstatus = models.CharField(max_length=30, default='available')
    videolink = models.CharField(max_length=100)

    class Meta:
        db_table = 'stations'

class UserBookRequest(models.Model):
    rid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=30)
    distric = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    evsname = models.CharField(max_length=30)
    status = models.CharField(max_length=20, default='created')
    statuss = models.CharField(max_length=30, default='created')
    price = models.CharField(max_length=20)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, db_column='sid')

    class Meta:
        db_table = 'userbookrequest'

class UserDetail(models.Model):
    uno = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=30)
    vehicle = models.CharField(max_length=30)
    udob = models.CharField(max_length=30)
    uphone = models.CharField(max_length=10)
    uemail = models.CharField(max_length=30)
    uusername = models.CharField(max_length=20)
    upassword = models.CharField(max_length=30)

    class Meta:
        db_table = 'userdetails'