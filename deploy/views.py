from django.shortcuts import render
from pathlib import Path
import joblib



# our home page view
def home(request):    
    return render(request, 'index.html')


# custom method for generating predictions
def getPredictions(Id,SepalWidthCm,PetalLengthCm,PetalWidthCm):
    #script_location = Path(__file__).absolute().parent
    #file_location = script_location /'Iris_lm.sav'
    #file_location = '/Users/Ritik mishra/Desktop/Django-project/deploy/deploy/Iris_lm.sav'
    model = joblib.load('Iris_lm.sav')
    #scaled = pickle.load(open("scaler.sav", "rb"))
    prediction = model.predict([[Id,SepalWidthCm,PetalLengthCm,PetalWidthCm]])
    
    # if prediction <= 0.5 :
    #     return "bed"
    # elif prediction >= 0.5:
    #     return "good"
    # else:
    return prediction
        

# our result page view
def result(request):
    Id = float(request.GET['Id'])
    SepalWidthCm = float(request.GET['SepalWidthCm'])
    PetalLengthCm = float(request.GET['PetalLengthCm'])
    PetalWidthCm = float(request.GET['PetalWidthCm'])

    result = getPredictions(Id,SepalWidthCm,PetalLengthCm,PetalWidthCm)

    return render(request, 'result.html', {'result':result})
