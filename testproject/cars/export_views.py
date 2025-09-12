from django.http import HttpResponse
import csv
from io import BytesIO
from openpyxl import Workbook
from rest_framework.decorators import api_view
from .models import Country, Manufacturer, Car, Comment


""" 
This view is for downloading files in csv or xlsx format.
View is common for all models. We specify the model (information) needed for downloading in the request body.
Choice model -> choice format (format=:csv or xlsx) ->
"""


@api_view(['GET'])
def export_data(request):
    model_name = request.GET.get('model')
    fmt = request.GET.get('format', 'csv')  # default CSV

    # Selecting a model by name
    models_dict = {
        'countries': Country,
        'manufacturers': Manufacturer,
        'cars': Car,
        'comments': Comment
    }

    if model_name not in models_dict:
        return HttpResponse(
            "Invalid model. Use one of: " + ", ".join(models_dict.keys()),
            status=400
        )

    model = models_dict[model_name]
    objects = model.objects.all()

    # We get a list of all model fields
    fields = [f.name for f in model._meta.fields]

    # We form it through the standard csv module
    if fmt == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{model_name}.csv"'

        writer = csv.writer(response)
        writer.writerow(fields)  # headers
        for obj in objects:
            writer.writerow([getattr(obj, f) for f in fields])

        return response

    # We form via openpyxl + BytesIO for correct download
    elif fmt == 'xlsx':
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = f'attachment; filename="{model_name}.xlsx"'

        wb = Workbook()
        ws = wb.active
        ws.append(fields)  # headers
        for obj in objects:
            ws.append([str(getattr(obj, f)) for f in fields])

        # Save to byte stream (correct download)
        output = BytesIO()
        wb.save(output)
        output.seek(0)
        response.write(output.getvalue())

        return response

    else:
        return HttpResponse("Invalid format. Use 'csv' or 'xlsx'.", status=400)
