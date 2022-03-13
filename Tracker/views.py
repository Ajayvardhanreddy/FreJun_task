from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.http import JsonResponse
from .models import TeamsData, TaskData


def home(request):
    return HttpResponse("Hello, Please use POSTMAN to use this API. It takes only JSON DATA.")


def login(request):
    login_details = json.loads(request.body.decode("utf-8"))
    if login_details['username'] == "team_leader":
        request.session['username'] = login_details['username']
    else:
        return JsonResponse({'success': "False", 'msg': 'Authentication failed. Wrong user! Team leaders can only access this route. Try again if you are team leader! '})


def create_team(request):
    if not request.session.get("login"):
        return JsonResponse({'success': "False", 'msg': 'Authentication failed. Login to use this API. Make a post JSON request with username as key and route /login/'})

    if request.method == 'POST':
        '''
        -> Example Json Data:
        {
            "team_name": "team_one",
            "team_members_ids": [
                "user_one", 
                "user_two",
                "user_three",
                "user_four",
                "user_five"
            ]
        }
        
        '''
        teams = json.loads(request.body.decode("utf-8"))

        # generating team_id using team_name and count of teams.
        teams_data = TeamsData.objects.values('team_id')
        unq = set()
        if teams_data:
            for i in teams_data:
                unq.add(i['team_id'])
            length = len(unq)+1
        else:
            length = 1
        team_id = teams['team_name'] + str(length)

        # Add data to database
        for member_id in teams["team_members_ids"]:
            obj = TeamsData(
                team_id=team_id,
                team_name=teams['team_name'],
                team_member_id=teams['team_name']+member_id,
                status_of_member=0
            )
            obj.save()
        return JsonResponse(teams)
    return HttpResponse('Only POST REQUEST accepted')


def get_availability(request):
    if not request.session.get("login"):
        return JsonResponse({'success': "False", 'msg': 'Authentication failed. Login to use this API. Make a post JSON request with username as key and route /login/'})

    team_id = json.loads(request.body.decode("utf-8"))
    availability = TeamsData.objects.filter(team_id=team_id['team_id']).order_by('id')
    if not availability:
        return HttpResponse('Wrong TeamID or there is no Team with this ID!')
    status_list = [True if i.status_of_member else False for i in availability]
    data = []
    for i in range(len(status_list)):
        member_id = 'member'+str(i+1)
        data.append({
            member_id: status_list[i]
        })
    response = {
        "success": True,
        "data": data
    }
    return JsonResponse(response)


def task(request):
    if not request.session.get("login"):
        update_fields = json.loads(request.body.decode("utf-8"))
        update_task = TaskData.objects.get(task_id=update_fields["task_id"])
        update_task.task_status = update_fields['status']
        update_task.save()
        return JsonResponse({"success": True, "msg": "status updated successfully"})
    if request.method == 'POST':
        '''
         -> Example Json Data:
            {
                "task_name": "task_one",
                "priority": "High",
                "start_date": "12-03-2022",
                "end_date": "12-03-2022",
                "team_member": "ajay",
                "status": "assigned"
            }
        '''
        taskjson = json.loads(request.body.decode("utf-8"))
        member_present = TeamsData.objects.filter(team_member_id=taskjson['team_member'])
        print(member_present, taskjson['team_member'])
        if member_present[0].status_of_member:
            return JsonResponse({"success": False, "msg": "team member is not available"})

        length = len(TaskData.objects.all())
        task_id = taskjson['task_name'] + str(length+1)

        # Add Data
        obj = TaskData(
                task_id=task_id,
                task_name=taskjson['task_name'],
                priority=taskjson['priority'],
                start_date=taskjson['start_date'],
                end_date=taskjson['end_date'],
                team_member=taskjson['team_member'],
                task_status=taskjson['status']
            )
        obj.save()
        update_status_obj = TeamsData.objects.get(team_member_id=taskjson['team_member'])

        update_status_obj.status_of_member = 1
        update_status_obj.save()
        return JsonResponse({"success": True, "msg": "Task created successfully"})
    elif request.method == 'PATCH':
        update_fields = json.loads(request.body.decode("utf-8"))
        update_task = TaskData.objects.get(task_id=update_fields["task_id"])
        update_task.priority = update_fields['priority'] if update_fields['priority'] else update_task.priority
        update_task.start_date = update_fields['priority'] if update_fields['start_date'] else update_task.start_date
        update_task.end_date = update_fields['end_date'] if update_fields['end_date'] else update_task.end_date
        update_task.team_member = update_fields['team_member'] if update_fields['team_member'] else update_task.team_member
        update_task.task_status = update_fields['status'] if update_fields['status'] else update_task.task_status
        update_task.save()
        return JsonResponse({"success": True, "msg": "Task updated successfully"})


def get_report(request):
    if not request.session.get("login"):
        return JsonResponse({'success': "False", 'msg': 'Authentication failed. Login to use this API. Make a post JSON request with username as key and route /login/'})

    date = json.loads(request.body.decode("utf-8"))['date']
    filter_task_date = TaskData.objects.filter(start_date=date)
    data = []
    for i in filter_task_date:
        data.append({
            "name": i.task_name,
            "team_member": i.team_member,
            "status": i.task_status
        })
    response = {
        'success': True,
        'data': data
    }
    return JsonResponse(response)


def logout(request):
    del request.session['username']
    return JsonResponse({"success": True, "msg": "Team Leader logged out successfully!"})

'''

DELETE FROM "Tracker_taskdata"
WHERE id=2;

SELECT * FROM public."Tracker_taskdata"
ORDER BY id 
DELETE FROM "Tracker_teamsdata";
'''