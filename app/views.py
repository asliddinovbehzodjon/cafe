from itertools import product
from django.shortcuts import render

# Create your views here.
from .serializer import CategorySerializer,ProductsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Category, Order, OrderItem,Products,ShippingInfo
from rest_framework.decorators import api_view
from rest_framework import generics


class AllCategory(APIView):
    def get(self,request):
        category=Category.objects.all()
        serializer=CategorySerializer(category,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class AllProducts(APIView):
    def get(self,request):
        products=Products.objects.all()
        serializer=ProductsSerializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class AboutCategoryProduct(APIView):
    def get(self,request,pk):
        try:
           category=Category.objects.get(id=pk)
           products=Products.objects.filter(category=category)
           serializer=ProductsSerializer(products,many=True)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data,status=status.HTTP_200_OK)
class Test(APIView):
    def get(self,request):
        from clickuz import ClickUz
        url = ClickUz.generate_url(order_id='172',amount='150000',return_url='http://behzodasliddinov.uz/')

        return Response({"url":url},status=status.HTTP_200_OK)
@api_view(['GET','POST'])
def SendTelegramBot(request,xabar):
        api2="5237355839:AAFOyuXByWribVN6BoFm9qPGAh8Lyhq1fl4"
        api1='5174285492:AAGMnWnrSg2bz37hrnAsDoEGeBP-gDerpv0'
        url1=f'https://api.telegram.org/bot{api1}/sendMessage?chat_id=5159670228&text={xabar}'
        url2=f'https://api.telegram.org/bot{api2}/sendMessage?chat_id=857727523&text={xabar}'  
        import requests
        requests.get(url1)
        requests.get(url2)
        return Response({'Message':'Send'},status=status.HTTP_200_OK) 

# @api_view(['GET','POST'])
# def order(request,user,phone,adress,id,quantity):
#         try:
#             product=Products.objects.get(id=id)
#             if Order.objects.filter(product=product,user=user).exists():
#                 Order.objects.filter(product=product,user=user).update(quantity=quantity)
#             else: 
#                 Order.objects.create(
#                     user=user,product=product,quantity=quantity
#                 )
#             return Response({"Order":"Added"},status=status.HTTP_200_OK)

#         except Products.DoesNotExist:
#              return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET','POST'])
def laststep(request,user,phone,adress,id,quantity):
    try:
       
        order=Order.objects.get(user=user)
        product=Products.objects.get(id=id)
        items=OrderItem.objects.create(order=order,product=product,quantity=quantity)
        data=order.orderitem_set.all()
        summa=data.all_summa
        info=ShippingInfo.objects.create(order=order,phone=phone,adress=adress)
        from clickuz import ClickUz


        url = ClickUz.generate_url(order_id=phone[1:],amount=summa,return_url='http://behzodasliddinov.uz/')

        return Response({"url":url},status=status.HTTP_200_OK)


    except Order.DoesNotExist:
        order=Order.objects.create(user=user)
        items=OrderItem.objects.create(order=order,product=product,quantity=quantity)
        data=order.orderitem_set.all()
        summa=data.all_summa
        info=ShippingInfo.objects.create(order=order,phone=phone,adress=adress)
        from clickuz import ClickUz


        url = ClickUz.generate_url(order_id=phone[1:],amount=summa,return_url='http://behzodasliddinov.uz/')

        return Response({"url":url},status=status.HTTP_200_OK)




    