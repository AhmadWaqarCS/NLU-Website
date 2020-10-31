from django.shortcuts import render
import nlu

def index(request):
	if request.POST:
		ty = request.POST['type']
		line = request.POST['value']
		pipeline =nlu.load("sentiment")
		prediction= pipeline.predict(line)
		return render(request, 'web/index.html', {'answer': prediction})
	else:
		return render(request, 'web/index.html', {})