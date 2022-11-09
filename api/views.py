from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer, TimingTodoSerializer
from .models import Todo
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action



@api_view(['GET', 'POST', 'PATCH'])
def home(request):
    if request.method == 'GET':

        return Response({
            'status': 200, 
            'message' : 'yes django restframework is working',
            'method_called': 'you called GET method'
        })
    elif request.method == 'POST':
        return Response({
            'status': 200, 
            'message' : 'yes django restframework is working',
            'method_called': 'you called POST method'
        })
    elif request.method == 'PATCH':
        return Response({
            'status': 200, 
            'message' : 'yes django restframework is working',
            'method_called': 'you called PATCH method'
        })
    else:
        return Response({
            'status': 400, 
            'message' : 'yes django restframework is working',
            'method_called': 'you called invalid method'
        })


@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True, 
                'message' : 'success data',
                'data': serializer.data
            })
        
        return Response({
                'status': False, 
                'message' : 'invalid data',
                'data': serializer.errors
            })
    
    except Exception as e:
        print(e)
    return Response({
            'status': False, 
            'message' : 'something went wrong',
        })

@api_view(['GET'])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSerializer(todo_objs, many=True)

    return Response({
        'status': True,
        'message':'todo fatched',
        'data': serializer.data
    })


@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'status': False,
                'message':'uid is required',
                'data': {}
            })

        obj = Todo.objects.get(uid = data.get('uid'))
        serializer = TodoSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True, 
                'message' : 'success data',
                'data': serializer.data
            })
        
        return Response({
                'status': False, 
                'message' : 'invalid data',
                'data': serializer.errors
            })
    except Exception as e:
        print(e)
    return Response({
            'status': False, 
            'message' : 'invalid uid',
            'data': {}
        })

class TodoView(APIView):
    def get(self, request):
        todo_objs = Todo.objects.all()
        serializer = TodoSerializer(todo_objs, many=True)

        return Response({
            'status': True,
            'message':'todo fatched',
            'data': serializer.data
            })
    
    def post(self, request):
        try:
            data = request.data
            serializer = TodoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True, 
                    'message' : 'success data',
                    'data': serializer.data
                })

            return Response({
                    'status': False, 
                    'message' : 'invalid data',
                    'data': serializer.errors
                })

        except Exception as e:
            print(e)
        return Response({
                'status': False, 
                'message' : 'something went wrong',
            })


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=['post'])
    def add_date_to_todo(self, request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True, 
                    'message' : 'success data',
                    'data': serializer.data
                    })
            
            return Response({
                'status': False, 
                'message' : 'invalid data',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
        return Response({
                'status': False, 
                'message' : 'invalid uid',
                'data': {}
            })






