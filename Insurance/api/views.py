from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.template.loader import render_to_string
import numpy as np
import joblib
import os
from .serializers import InsuranceSerializer
import threading
# get the path to the pickeled model file
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','Model','InsuranceCostPredictor.pkl')

# load the pickeled model
model = joblib.load(model_path)

@api_view(['POST'])
def predict(request):
    if request.method == 'POST':
        # deserialize the input data from the request
        serializer = InsuranceSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            #  convert input data to input format for model
            input_data = tuple(serializer.validated_data.values())
            input_data_as_numpy_array = np.asarray(input_data)
            input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
            print(input_data_reshaped)
        
        #make a prediction using the model
        prediction = model.predict(input_data_reshaped)

        #return the prediction as a JSON response
        return Response(prediction)
    


@api_view(['POST'])
def send_email_api(request):
    print("sending mail")
    try:
        # Parse the JSON data from the request
        data = request.data

        # Extract the necessary fields from the JSON payload
        username = data.get('username')
        email = data.get('email')
        age = data.get('age')
        sex = data.get('sex')
        bmi = data.get('bmi')
        children = data.get('children')
        smoker = data.get('smoker')
        region = data.get('region')
        result = data.get('result')

        # Ensure all required fields are present
        if not all([username, email, age, sex, bmi, children, smoker, region, result]):
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare context for the email template
        context = {
            'username': username,
            'age': age,
            'sex': sex,
            'bmi': bmi,
            'children': children,
            'smoker': smoker,
            'region': region,
            'result': result
        }

        # Render email template with the context
        subject = 'Your Health Insurance Details'
        from_email = 'mr.goku.0619@gmail.com'  # Replace with your actual email
        html_content = render_to_string('mail.html', context)

        # Send the email using send_mail
        def send_mail_asyn(subject,from_email,email,html_content):
            send_mail(
                subject,
                '', 
                from_email,
                [email], 
                fail_silently=False,
                html_message=html_content 
            )

        threading.Thread(target=send_mail_asyn,args=(subject,from_email,email,html_content)).start()

        return Response({'message': 'Email sent successfully!'}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)