from django.shortcuts import render
#from django.http import HttpResponse
from .models import UpcomingEvent, ThingsHappening, Uploads, Album, Gallery, Devotion
import datetime
from django.shortcuts import get_object_or_404



#This function gets events that are not overdue. Only evnts not held are displayed
def get_valid_upcoming_events(get_upcomingevents):
    todays_date = datetime.date.today()
    valid_upcomingevents = []
    for item in get_upcomingevents:
        date_diff = (item.start_day - todays_date).days
        if date_diff > 0 :
            valid_upcomingevents.append(item)
        else :
            pass
    return valid_upcomingevents

def inner_right_upcoming():
    get_all_upcomingevents=UpcomingEvent.objects.filter(make_visible= True).order_by('start_day')
    all_valid_upcomingevents = get_valid_upcoming_events(get_all_upcomingevents)
    
    return all_valid_upcomingevents


def inner_things_happening():
    get_all_things_happening=ThingsHappening.objects.filter(make_visible= True).order_by('update_date')
    
    return get_all_things_happening 


def home(request):
    get_latest_albums = Album.objects.filter(make_it_visible=True, homepage_visible=True).order_by('create_date')[:2]
    get_album_cover = Gallery.objects.filter(is_album_cover = True)
    get_latest_devotions = Devotion.objects.filter(make_visible=True).order_by('-create_date')[:2]
    latest_devotion = get_latest_devotions[0]
    sec_latest_devotion = get_latest_devotions[1]
    # Get count of visible events
    getNum_upcomingevents=UpcomingEvent.objects.filter(make_visible= True).count()
    
    # Get count of activities that can be shown in homepage
    getNum_things_happening=ThingsHappening.objects.filter(show_in_homepage= True).count()
    
    # if count greater than 3. Then get only latest three upcoming events
    if getNum_upcomingevents > 3:
        get_upcomingevents = UpcomingEvent.objects.filter(make_visible= True).order_by('start_day')[:3]
        # Get valid events
        valid_upcomingevents = get_valid_upcoming_events(get_upcomingevents)
    else:
        get_upcomingevents = UpcomingEvent.objects.filter(make_visible= True).order_by('start_day')
        # Get valid events 
        valid_upcomingevents = get_valid_upcoming_events(get_upcomingevents)
        
        
    if getNum_things_happening > 4:
        things_happening = ThingsHappening.objects.filter(show_in_homepage = True).order_by('-update_date')[:4]
        #print(things_happening)
    else:
        things_happening = ThingsHappening.objects.filter(show_in_homepage = True).order_by('update_date')
        #print(things_happening)
    print(get_latest_devotions[0].devotion_title)
    context = {
           'valid_upcomingevents':valid_upcomingevents,
           'things_happening':things_happening,
           'get_album_cover':get_album_cover,
           'get_latest_albums':get_latest_albums,
           'get_latest_devotions':get_latest_devotions,
           'latest_devotion':latest_devotion,
           'sec_latest_devotion':sec_latest_devotion,
        }
    
    return render(request, 'core/index.html', context)
    

def about(request, about_type):
    
    context = {
               
        'about_type': about_type,
        'inner_right_upcoming' : inner_right_upcoming,
        'inner_things_happening':inner_things_happening,
        }
    
    return render(request, 'core/about.html', context)

def ministry(request, ministry_type):
    
    context = {
               
        'ministry_type': ministry_type,
        'inner_right_upcoming' : inner_right_upcoming,
        'inner_things_happening':inner_things_happening,
        }
    
    return render(request, 'core/ministry.html', context)

def devotionarticle(request, devotion_id):
    get_devotion = Devotion.objects.filter(pk = devotion_id)
    
    print(get_devotion)
    context = {
        'devotion_id':devotion_id,
        'get_devotion': get_devotion,

        }
    
    return render(request, 'core/devotionarticle.html', context)

def contact(request):
    
    context = {

        }
    
    return render(request, 'core/contact.html', context)

def albumgallery(request, album_id):
    get_album_images = Gallery.objects.filter(pic_album = album_id).order_by("create_date")
    album = Album.objects.get(id = album_id)
    print(album)
    context = {
        'album' : album, 
        'get_album_images' : get_album_images,
        }
    
    return render(request, 'core/albumgallery.html', context)

def resources(request, resources_type):   
   
    context = {
             
        'resources_type': resources_type,
        'inner_right_upcoming' : inner_right_upcoming,
        'inner_things_happening':inner_things_happening,
        }
    
    if resources_type == "media":
        get_album = Album.objects.filter(make_it_visible = True).order_by("create_date")
        get_album_cover = Gallery.objects.filter(is_album_cover = True)
#         print(get_album_cover)
#         for item in get_album_cover:
#             print(item.pic_album.id)
#         print("foo bar")
        context ['get_album'] = get_album
        context ['get_album_cover'] = get_album_cover
        
    if resources_type == "downloads":
        get_uploads = Uploads.objects.filter(make_visible = True).order_by("create_date")
        context ['get_uploads'] = get_uploads
    
    if resources_type == "devotion":
        get_devotions = Devotion.objects.filter(make_visible = True).order_by("-create_date")
        context ['get_devotions'] = get_devotions
    
    return render(request, 'core/resources.html', context)

def whatwedo(request):
    
    context = {
        'inner_right_upcoming' : inner_right_upcoming,
        'inner_things_happening':inner_things_happening,

        }
    
    return render(request, 'core/whatwedo.html', context)

def building(request):
    
    context = {

        }
    
    return render(request, 'core/building.html', context)

def happening(request, happening_type):
    
    if happening_type == 'upcoming' :
        get_all_upcomingevents=UpcomingEvent.objects.all().order_by('start_day')
        all_valid_upcomingevents = get_valid_upcoming_events(get_all_upcomingevents)
        context = {
            'happening_type':happening_type,
            'all_valid_upcomingevents':all_valid_upcomingevents,
            'inner_right_upcoming' : inner_right_upcoming,
            'inner_things_happening':inner_things_happening,
            }
    if happening_type == 'whatishappening' :
        get_all_things_happening=ThingsHappening.objects.all().order_by('create_date')
        context = {
            'happening_type':happening_type,
            'inner_right_upcoming' : inner_right_upcoming,
            'inner_things_happening':inner_things_happening,
            'get_all_things_happening':get_all_things_happening,
            }
    return render(request, 'core/happening.html', context)

def happeningdetail(request,happeningdetail_id,happeningdetail_type):
    if happeningdetail_type == 'upcoming' :
        get_happeningdetail = get_object_or_404 (UpcomingEvent, pk = happeningdetail_id)
        
    if happeningdetail_type == 'whatishappening' :
        get_happeningdetail = get_object_or_404 (ThingsHappening, pk = happeningdetail_id)

        pass
    
#     print( get_happeningdetail.happening_thing_note)
#     if "http://" in get_happeningdetail.happening_thing_note :
#         get_happeningdetail.happening_thing_note = get_happeningdetail.happening_thing_note.replace("http://", "")
#     else:
#         pass
    
    context = {
        'happeningdetail_type':happeningdetail_type,
        'get_happeningdetail' :get_happeningdetail,
        }
    
    return render(request, 'core/happeningdetail.html', context)
