from django.shortcuts import render
from . forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import Approvals
from . serializer import ApprovalsSerializer
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd

# Create your views here.

class ApprovalsView(viewsets.ModelViewSet):
        queryset = Approvals.objects.all()
        serializer_class = ApprovalsSerializer
        
@api_view(["POST"])
def approvereject(request):
	try:
		mdl=joblib.load('Loan_Model.pkl')
		#mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
		mydata=request.data
		unit=np.array(list(mydata.values()))
		unit=unit.reshape(1,-1)
		scalers=joblib.load('scalers.pkl')
		x=scalers.transform(unit)
		y_pred=mdl .predict(x)
		y_pred=(y_pred>0.58)
		newdf=pd.DataFrame(y_pred, columns=['Status'])
		newdf=newdf.replace({True:'Approved', False:'Rejected'})
		return JsonResponse('Your Status is {}'.format(newdf), safe=False)
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)