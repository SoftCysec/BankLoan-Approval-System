from django.forms import ModelForm
from . models import Approvals

class MyForm(ModelForm):
	class Meta:
		model=Approvals
		fields = '__all__'