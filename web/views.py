from django.shortcuts import render
import os
os.system('! apt-get update -qq > /dev/null')
os.system('! apt-get install -y openjdk-8-jdk-headless -qq > /dev/null')

os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin:" + os.environ["PATH"]
import nlu


def index(request):
	if request.POST:
		ty = request.POST['type']
		line = request.POST['value']
		pipeline = nlu.load(ty)
		prediction = pipeline.predict(line)
		return render(request, 'web/index.html', {'answer': prediction})
	else:
		return render(request, 'web/index.html', {})