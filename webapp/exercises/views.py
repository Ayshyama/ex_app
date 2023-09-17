import random

import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from .models import *


def index_page(request):
    return render(request, 'index.html')


def roadmap_page(request):
    return render(request, 'roadmap.html')


def get_exercise(request):
    all_exercises = {
        'Lists': Lists.objects.all(),
        'Dictionaries': Dictionaries.objects.all(),
        'Tuples': Tuples.objects.all(),
        'Sets': Sets.objects.all(),
        "String Manipulation": StringManipulation.objects.all(),
        "Indexing And Slicing": IndexingAndSlicing.objects.all(),
        "Mutable And Immutable Types": MutableAndImutableTypes.objects.all(),
        'Data Types': DataTypes.objects.all(),
        'Methods Of Types': MethodsOfTypes.objects.all(),
        'Comprehension': Comprehension.objects.all(),
        'Exceptions': Exceptions.objects.all(),
        'Local And Global Scope': LocalAndGlobalScope.objects.all(),
        'Closures': Closures.objects.all(),
        'Short Circuit Evaluation': ShortCircuitEvaluation.objects.all(),
    }
    context = {
        'all_exercises': all_exercises
    }
    print(all_exercises['Closures'])

    return render(request, 'exercise.html', context)


def get_random_exercise(request):
    models = [
        Lists, Dictionaries, Tuples, Sets, StringManipulation,
        IndexingAndSlicing, MutableAndImutableTypes, DataTypes,
        MethodsOfTypes, Comprehension, Exceptions, LocalAndGlobalScope,
        Closures, ShortCircuitEvaluation
    ]

    chosen_model = random.choice(models)

    exercises = list(chosen_model.objects.values_list('exercise_text', flat=True))

    if not exercises:
        return JsonResponse({"exercise": ""})

    chosen_exercise = random.choice(exercises)

    return JsonResponse({"exercise": chosen_exercise})


def get_hint_from_chatgpt(request):
    exercise = request.GET.get('exercise', None)
    if not exercise:
        return JsonResponse({"error": "Exercise text not provided."})

    headers = {
        'Authorization': f'Bearer {settings.CHATGPT_API_KEY}',
        'Content-Type': 'application/json',
    }

    prompt_text = f"Imagine you are Python expert and you help to teach this topic. " \
                  f"How would you provide a hint for the following Python task without revealing the full solution: '{exercise}'? " \
                  f"Answer only with hint text starting your 'Hint: '. After hint provide a link to documentation of this topic"

    data = {
        "model": "gpt-3.5-turbo-0613",
        "messages": [{"role": "user", "content": prompt_text}],
        "max_tokens": 150
    }

    try:
        response = requests.post(settings.CHATGPT_API_URL, headers=headers, json=data)
        response.raise_for_status()

        data = response.json()
        message_response = data.get('choices')[0].get('message', {}).get('content', '').strip()
        # Insert a line break before the "Check out the Python documentation" part
        message_response = message_response.replace("Check out the Python documentation",
                                                    "<br>Check out the Python documentation")

        return JsonResponse({"hint": message_response.strip()})

    except requests.RequestException as e:
        print(response.text)
        return JsonResponse({"error": f"Error communicating with OpenAI: {str(e)}"})





