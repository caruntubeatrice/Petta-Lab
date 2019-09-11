# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pressure:
    con = MySQLdb.connect(host = "127.0.0.1",
                          user = "root",
                          passwd = "bepa26betty98",
                          db = "sample")