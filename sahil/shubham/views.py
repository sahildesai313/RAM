from rest_framework import status
from rest_framework.response import Response
from shubham.models import Shubham
from shubham.serializers import ShubhamSerializer
from django.http import Http404
from rest_framework.views import APIView





class SnippetList(APIView):

    def get(self,request,format=None):
        x=Shubham.objects.all()
        serializer=ShubhamSerializer(x,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=ShubhamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Shubham.objects.get(pk=pk)
        except Shubham.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ShubhamSerializer(snippet)
        return Response(serializer.data)

# class SnippetDetail(APIView):
    
#     def get_object(self,pk):
#         try:
#             print(pk,'pk')
#             a = Shubham.objects.get(pk=pk)
#             print("a", a)

#         except  Shubham.DoesNotExist:       
#             raise Http404
        
#     def get(self, pk):
#         print('Foriegn_Key: ', pk)
#         x = self.get_object(pk)
#         # serializer=ShubhamSerializer(x)
#         return Response({'x': x})
    
    
#     # def put(self,pk,request,format=None):
#     #     x=self.get_object(pk)
#     #     serializer=ShubhamSerializer(x,data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data)
#     #     return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
#     # def delete(self,pk,request,format=None):
#     #     x=self.get_object(pk)
#     #     x.delete()
#     #     return Response(status=status.HTTP_204_NO_CONTENT)

























































"""

@api_view(['GET','POST'])

def shubham_List(request,format=None):
    
    if request.method == 'GET':
        x= Shubham.objects.all()
        serializer=ShubhamSerializer(x,many=True)
        return Response(serializer.data)
    
    
    elif request.method == 'POST':
        serializer=ShubhamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
@api_view(['GET','PUT','DELETE'])



def shubham_details(request,pk,format=None):
    
    
    try :
        x= Shubham.object.get(pk=pk)
    except Shubham.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='GET':
        serializer=ShubhamSerializer(x)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=ShubhamSerializer(x,data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method=='DELETE':
        Shubham.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        """