from django.shortcuts import render
from test_app.models import Test_model
from django.http import JsonResponse


def home(request):

    fields = Test_model._meta.get_fields()[1:]
    return render(request, 'home.html', {'fields':fields})

# Create your views here.
def process_ajax(request):

    draw = request.GET['draw']
    start = int(request.GET['start'])
    length = int(request.GET['length'])
    order_column = int(request.GET['order[0][column]'])
    order_direction = '' if request.GET['order[0][dir]'] == 'desc' else '-'
    column = [i.name for n, i in enumerate(Test_model._meta.get_fields()) if n == order_column][0]
    global_search = request.GET['search[value]']
    all_objects = Test_model.objects.all()

    columns = [i.name for i in Test_model._meta.get_fields()][1:]
    objects = []
    for i in all_objects.order_by(order_direction + column)[start:start + length].values():
        ret = [i[j] for j in columns]
        objects.append(ret)
    filtered_count = all_objects.count()
    total_count = Test_model.objects.count()
    return JsonResponse({
        "sEcho": draw,
        "iTotalRecords": total_count,
        "iTotalDisplayRecords": filtered_count,
        "aaData": objects,

    })