from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views import View
from django.http import HttpResponse


class MainView(View):

    def get(self, request):
        return render(request, "cashmachine.html", {'disabled': ''})

    def post(self, request):
        notes = []
        available_notes = [100, 50, 20, 10]

        wanted_amount = request.POST.get("valueof")

        if wanted_amount[0] is not "[" and wanted_amount[0] is not "Y":
            wanted_amount = int(wanted_amount)

            if wanted_amount % 10 == 0 and wanted_amount > 0:
                for available_note in available_notes:
                    note_amount = int(wanted_amount / available_note)
                    for i in range(0, note_amount):
                        notes.append(available_note)
                        wanted_amount -= available_note
            else:
                return render(request, "cashmachine.html", {'notes': str(notes), 'disabled': 'disabled'})
            return render(request, "cashmachine.html", {'notes': str(notes),  'disabled': 'disabled'})
        else:
            return render(request, "cashmachine.html", {'notes': "You already received your notes!", 'disabled': 'disabled'})

