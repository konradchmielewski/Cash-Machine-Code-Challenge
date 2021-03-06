from django.shortcuts import render
from django.views import View


class MainView(View):

    def get(self, request):
        return render(request, "cashmachine.html", {'disabled': ''})

    def post(self, request):

        wanted_amount = request.POST.get("input_value")

        if not wanted_amount:
            return render(request, "cashmachine.html", {'notes': "[Empty Set]", 'disabled': 'disabled'})

        try:
            wanted_amount = int(wanted_amount)

            if wanted_amount > 0:
                if wanted_amount % 10 == 0:
                    notes = get_notes_from_amount(wanted_amount)
                    return render(request, "cashmachine.html", {'notes': str(notes), 'disabled': 'disabled'})
                return render(request, "cashmachine.html", {'notes': "NoteUnavailableException",
                                                            'disabled': 'disabled'})
            return render(request, "cashmachine.html",
                          {'notes': "InvalidArgumentException", 'disabled': 'disabled'})
        except ValueError:
            return render(request, "cashmachine.html",
                          {'notes': "InvalidArgumentException", 'disabled': 'disabled'})


def get_notes_from_amount(wanted_amount):

    available_notes = [100, 50, 20, 10]
    notes = []
    for available_note in available_notes:
        note_amount = int(wanted_amount / available_note)
        for i in range(0, note_amount):
            notes.append(available_note)
            wanted_amount -= available_note

    return notes
