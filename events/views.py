import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from .models import Event

# -----------------------------
# 1️⃣ Summoning Spell: create_event
# -----------------------------
@csrf_exempt
def create_event(request):
    if request.method == "POST":
        data = json.loads(request.body)
        event = Event.objects.create(
            name=data["name"],
            description=data["description"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
        )
        return JsonResponse({"message": "Event created", "id": str(event.id)})
    return JsonResponse({"error": "Invalid method"}, status=400)

# -----------------------------
# 2️⃣ Scrying Spell: get_all_events
# -----------------------------
def get_all_events(request):
    if request.method == "GET":
        events = Event.objects.all()
        data = [
            {
                "id": str(e.id),
                "name": e.name,
                "description": e.description,
                "location": e.location,
                "start_date": e.start_date,
                "end_date": e.end_date,
            } for e in events
        ]
        return JsonResponse(data, safe=False)
    return JsonResponse({"error": "Invalid method"}, status=400)

# -----------------------------
# 3️⃣ Lens Spell: get_event
# -----------------------------
def get_event(request, event_id):
    if request.method == "GET":
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return JsonResponse({"error": "Event not found"}, status=404)
        data = {
            "id": str(event.id),
            "name": event.name,
            "description": event.description,
            "location": event.location,
            "start_date": event.start_date,
            "end_date": event.end_date,
        }
        return JsonResponse(data)
    return JsonResponse({"error": "Invalid method"}, status=400)

# -----------------------------
# 4️⃣ Transforming Spell: update_event
# -----------------------------
@csrf_exempt
def update_event(request, event_id):
    if request.method == "PATCH":
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return JsonResponse({"error": "Event not found"}, status=404)
        data = json.loads(request.body)
        event.name = data.get("name", event.name)
        event.description = data.get("description", event.description)
        event.location = data.get("location", event.location)
        event.start_date = data.get("start_date", event.start_date)
        event.end_date = data.get("end_date", event.end_date)
        event.save()
        return JsonResponse({"message": "Event updated"})
    return JsonResponse({"error": "Invalid method"}, status=400)

# -----------------------------
# 5️⃣ Vanishing Spell: delete_event
# -----------------------------
@csrf_exempt
def delete_event(request, event_id):
    if request.method == "DELETE":
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return JsonResponse({"error": "Event not found"}, status=404)
        event.delete()
        return JsonResponse({"message": "Event deleted"})
    return JsonResponse({"error": "Invalid method"}, status=400)

# -----------------------------
# HTML Pages
# -----------------------------
def home_page(request):
    return render(request, "events/home.html")

def event_list_page(request):
    events = Event.objects.all()
    return render(request, "events/event_list.html", {"events": events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "events/event_detail.html", {"event": event})

def about_page(request):
    return render(request, "events/about.html")