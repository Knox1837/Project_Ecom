from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from Ecom_app.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
# Create your views here.

class ApiResponse():
    def success_response(self, message, code, data=dict()):
        context={
            "message": message,
            "status code": code,
            "data": data,
            "error":[]
        }
        return context

class CategoryApiView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return Response(category_serializer.data, status=status.HTTP_200_OK)

class ProductApiView(APIView):
    def get(self, request):
        products=Product.objects.all()
        try:
            product_serialize=ProductSerializer(products, many=True)
            return Response(ApiResponse.success_response(None, "Products", 200 ,product_serialize.data), status= status.HTTP_200_OK) # or (message="Product List", code=200, data=product_serialize.data)
        except Product.DoesNotExist:
            return Response({"msg":"Product does not exist"}, status= status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        data= request.data     # if getting data from a form request.POST.get(<<varname>>) is used
        product_serialize = ProductSerializer(data=data)
        
        if product_serialize.is_valid():
            product_serialize.save()
            return Response(ApiResponse.success_response(None, "Product Added", 200, data))
            #return Response({'msg':'Product Added Successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(product_serialize.errors, status= status.HTTP_400_BAD_REQUEST)

class ProductApiIdView(APIView):# update
    def get_object(self, id):
        '''this function returns the object of product'''
        try:
            product=Product.objects.get(id=id)# first id = database id and 2nd id = parameter id 
            return product
        except Product.DoesNotExist:
            return None
        
    def get(self, request, id):
        instance = self.get_object(id)
        if not instance:
            return Response({'msg': "Data Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        instance = self.get_object(id)
        if not instance:
            return Response({'msg': "Data Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated Successfully', 'data': serializer.data},status=status.HTTP_200_OK )
        else:
            return Response({'msg':'Data not Updated','error': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)


    def delete(self, request, id):
        instance = self.get_object(id)
        if not instance:
            return Response({'msg': "Data Not found"}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({'msg':'Item deleted Successfully'}, status=status.HTTP_200_OK)

class LoginApiView(APIView):
    def get(self, request):
        pass
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'msg':'Login Successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': "Failed Login request"}, status=status.HTTP_406_NOT_ACCEPTABLE)

class RegisterApiView(APIView):
    def get(self, request):
        pass
        
    def post(self, request):
        try:
            data = request.data
            first_name = data['first_name'] 
            last_name = data['last_name']
            email = data['email']
            username = data['username']
            password = data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            
            test= authenticate(username=username, password=password)
            if test:
                return Response({'msg': "User Created Sucessfully"}, status=status.HTTP_200_OK)
            else:
                return Response({'msg': "Registration Failed"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except:
            return Response({"Msg": "Error!"}, status=status.HTTP_406_NOT_ACCEPTABLE)