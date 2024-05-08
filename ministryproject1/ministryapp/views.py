from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterModelSerializer,LoginModelSerializer,ProfileModelSerializer,PasswordChangeSerializer,SendMailPasswordResetSerializer,DoPasswordResetSerializer,CourseSerializer,VideoSerializer,TimerSerializer
from django.contrib.auth import authenticate
from .renderer import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
#from .utils import get_graph,get_plot,create_pie_chart,get_pie_chart
from django.http import HttpResponse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
from django.http import JsonResponse
from django.http import HttpResponse
import base64
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from io import BytesIO
import base64
from matplotlib.animation import FuncAnimation
import tempfile
import os
from random import randint
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *

from django.shortcuts import render
#from .utils import animate_3d_data,generate_animation,generate_angle_visualization

from .models import Course, Video
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import generics

############
# score=0
# def guess_number(request):
#     global score
#     if request.method == 'POST':
#         user_guess = int(request.POST.get('user_guess'))
#         random_number = random.randint(1, 10)
        
#         if user_guess == random_number:
#             message = f'Congratulations! Your guess is correct. Score: {score}'
#             score += 1
#         elif user_guess < random_number:
#             message = 'Your guess is too low.'
#         else:
#             message = 'Your guess is too high.'
        
#         return JsonResponse({'message': message})
# def guess_number(request):
#   if request.method == 'POST':
#     user_guess = int(request.POST['guess'])

#     if not request.session.get('random_number'):
#       request.session['random_number'] = randint(1, 20)
#     random_number = request.session.get('random_number')

#     if user_guess == random_number:
#       message = "Congratulations! You guessed the number!"
#       del request.session['random_number']
#     else:
#       message = f"Sorry, the number is {'higher' if user_guess < random_number else 'lower'}."

#     return JsonResponse({'message': message})  # Return JSON response
#   else:
#     message = ""
#     request.session.get('random_number', None)  # Clear random number if exists

#   return JsonResponse({'message': message})  # Empty JSON for initial load


def my_animation_view(request):
    t = np.linspace(0, 2*np.pi, 100)
    x = np.sin(t)
    y = np.cos(t)
    z = t
    animation_data = animate_3d_data(x, y, z)
    context = {'animation_data': animation_data}
    return render(request, 'ministryapptemp/matrix.html', context)

def animation_view(request):
     # Generate data for sine function
    x = np.linspace(0, 2 * np.pi, 100)
    y_sine = np.sin(x)
    y_cos=np.cos(x)
    

    # Generate animation for sine and cosine functions
    animation_data = generate_animation(x, y_sine,y_cos)

    # Pass animation data to the template context
    context = {'animation_data': animation_data}

    # Render the template with the context data
    return render(request, 'ministryapptemp/sine.html', context)



@csrf_exempt
def generate_angle_visualization_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_angle = data.get('angle')
            if user_angle is not None:
                # Generate angle visualization
                image_data = generate_angle_visualization(user_angle)
                # Return image as HTTP response
                return HttpResponse(image_data, content_type='image/png')
            else:
                return HttpResponse('Angle value is missing', status=400)
        except Exception as e:
            return HttpResponse(str(e), status=500)
    else:
        return HttpResponse('Method not allowed', status=405)
#############


def Home(request):
    return render(request,'ministryapptemp/base.html')

def graphform(request):
    return render(request,'ministryapptemp/barform.html')
def pieform(request):
    return render(request,'ministryapptemp/pieform.html')



@csrf_exempt   
def generate_pie_chart(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            chart_type = data.get('chart_type')
            labels = data.get('labels', '')
            sizes_data = data.get('sizes', '')

            if not labels or not sizes_data:
                return HttpResponse("Labels or sizes are missing", status=400)

            labels = labels.split(',')
            sizes = [int(size.strip()) for size in sizes_data.split(',') if size.strip().isdigit()]

            if len(labels) != len(sizes):
                return HttpResponse("The number of labels and sizes must match", status=400)

            fig, ax = plt.subplots()
            if chart_type == 'pie':
                ax.pie(sizes, labels=labels, autopct='%1.1f%%')
            elif chart_type == 'line':
                ax.plot(labels, sizes)  # Assuming labels here are categorical
                ax.legend(labels)
            else:
                return HttpResponse("Invalid chart type", status=400)

            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            plt.close(fig)
            buf.seek(0)

            return HttpResponse(buf.read(), content_type='image/png')
        except ValueError as e:
            return HttpResponse(f"Error processing data: {str(e)}", status=400)
        except Exception as e:
            return HttpResponse(f"Unexpected error: {str(e)}", status=500)
    else:
        return HttpResponse("Invalid request method", status=405)
    # Create a pie chart
    # labels = 'Red', 'Blue', 'Green'
    # sizes = [215, 130, 245]
    # fig, ax = plt.subplots()
    # ax.pie(sizes, labels=labels, autopct='%1.1f%%')

    # # Save the plot to a BytesIO object
    # buf = io.BytesIO()
    # plt.savefig(buf, format='png')
    # plt.close(fig)
    # # Rewind the buffer
    # buf.seek(0)

    # # Construct an HTTP response with the image as content
    # return HttpResponse(buf.read(), content_type='image/png')

def generate_line_chart(request):
    # Data for plotting
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    # Create a new figure
    fig, ax = plt.subplots()
    ax.plot(x, y, label='Square Numbers', marker='o')

    # Set labels and title
    ax.set_xlabel('X values')
    ax.set_ylabel('Y values')
    ax.set_title('Simple Line Plot')
    ax.legend()

    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)  # Close the plot figure to free up memory

    # Rewind the buffer to the beginning so we can read its content
    buf.seek(0)

    # Construct an HTTP response with the image data in PNG format
    return HttpResponse(buf.read(), content_type='image/png')

def pie_chart_view(request):
    if request.method == 'POST':
        x_values = request.POST.get('x', '')
        y_values = request.POST.get('y', '')
        
        x = x_values.split(',') if x_values else []
        y = [float(i) for i in y_values.split(',')] if y_values else []

        if x and y and (len(x) == len(y)):
            fig=create_pie_chart(x,y)
            chart = get_pie_chart(fig)
            return render(request, 'ministryapptemp/bar.html', {'chart': chart})
            
        else:
            return render(request, 'ministryapptemp/pieform.html', {'error': 'The number of labels and values must match and must not be empty.'})
    return render(request, 'ministryapptemp/pieform.html')

    # labels = 'Red', 'Blue', 'Green', 'Yellow'
    # sizes = [215, 130, 245, 210]
    # fig = create_pie_chart(labels, sizes)
    # chart = get_pie_chart(fig)
    # return render(request, 'ministryapptemp/bar.html',context= {'chart': chart})

def graph_view(request):
    x=[]
    y=[]
    if request.method=='POST':
        item1=request.POST.get('x','')
        item2=request.POST.get('y','')
        
        x = item1.split(',') if item1 else []
        y = [int(value) for value in item2.split(',')] if item2 else []
        
        if len(x) == len(y):
            chart = get_plot(x, y)
            return render(request, 'ministryapptemp/bar.html', {'chart': chart})
        else:
            return render(request, 'ministryapptemp/barform.html', {'error': 'The number of x and y values must match.'})
    return render(request, 'ministryapptemp/barform.html')
        # print(item1)
        # print(item2)
        
        # li1=item1.split(',')
        # li2=item2.split(',')
       
        # x.append(li1)
        # x.append(li2)
        # # x=['apple','ball']
        # # y=[34,45]
        # chart=get_plot(x,y)
        # return render(request,'ministryapptemp/bar.html',context={'chart':chart})
def generate_matrix_chart(request):
    if request.method == 'POST':
        # Get the matrix data from the POST request
        matrix_data = request.POST.get('matrix_data')
        
        # Convert the input string to a 2D array
        matrix = np.array([list(map(float, row.split(','))) for row in matrix_data.strip().split('\n')])

        # Create a new figure
        fig, ax = plt.subplots()

        # Plot the matrix as a heatmap
        im = ax.imshow(matrix, cmap='viridis')

        # Add color bar
        cbar = ax.figure.colorbar(im, ax=ax)

        # Set labels and title
        ax.set_xlabel('X values')
        ax.set_ylabel('Y values')
        ax.set_title('Heatmap of Matrix')

        # Save the plot to a BytesIO object
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        plt.close(fig)  # Close the plot figure to free up memory

        # Rewind the buffer to the beginning so we can read its content
        buf.seek(0)

        # Construct an HTTP response with the image data in PNG format
        return HttpResponse(buf.read(), content_type='image/png')
    else:
        return HttpResponse("Please submit a POST request with matrix data.")

  
def matrixform(request):
    return render(request, 'ministryapptemp/matrix.html', {'plot_image': None})


    
#generate token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# Create your views here.

class RegisterModelView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=RegisterModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Registration successfull'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class LoginModelView(APIView):
    def post(self,request,format=None):
        serializer=LoginModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
         email=serializer.data.get('email')
         password=serializer.data.get('password')
         
         user=authenticate(email=email,password=password)
         if user is not None:
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'login successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ProfileModelView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        serializer=ProfileModelSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    

class PasswordChangeView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serializer=PasswordChangeSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'password changed successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class SendMailPasswordResetView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=SendMailPasswordResetSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Email send successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class DoPasswordResetView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,uid,token,format=None):
        serializer=DoPasswordResetSerializer(data=request.data,context={
            'uid':uid,
            'token':token
        })
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'password reset successfully'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

def course_detail(request,classnumber=None):
    classnumber=None
    if classnumber is not None:
        classname=Course.objects.get(classnumber=classnumber)
        videos=Video.objects.filter(course=classname)
        context={
            'videos':videos,
            'classname':classname
        }
    else:
        classname=Course.objects.all()
        videos=Video.objects.all()
        context={
            'videos':videos,
            'classname':classname
        }
    return render(request,'ministryapptemp/course_detail.html',context)

@api_view(['POST'])
def save_time(request):
    if request.method == 'POST':
        user = request.user
        time = request.data.get('time')
        serializer = TimerSerializer(data={'user': user.id, 'time': time})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Time saved successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def course_detail(request, classnumber=None):
#     if classnumber is not None:
#         coursename = get_object_or_404(Course, classnumber=classnumber)
#         serializer = CourseSerializer(coursename)
        
#     else:
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
    
#     return Response(serializer.data)

