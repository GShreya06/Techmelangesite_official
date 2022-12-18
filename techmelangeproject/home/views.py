from django.http import HttpResponse
from django.shortcuts import render
from .models import festdesc
from .models import events
# Create your views here.


def home(request):
    # for only first element use first
    #for all objects use all
    a=festdesc.objects.all().first(); 
    # a1=festdesc.objects.all()[0][1];
    
    print(a)
    # print(a1)
    # for i in a: 
    #     # for taking values from database use loop
    #     print(i.fest_name) 
    #     print(i.fest_desc)
    #     print(i.fest_bg)
    
    # b=events.objects.all();
    # print(b)
    # for i in b:
    #     print(i.e_name)
    #     print(i.e_desc)
    #     print(i.e_img)
    #     print(i.e_frm)
        
    
    

    str = "ENIAC-The Computer Science Society, Department of Computer Science, Shaheed Rajguru College Of Applied Sciences for Women, University Of Delhi presents its Annual Techfest - TECH MELANGE'23."
    str1 = "As the name suggests, Tech Melange is the perfect blend of hosting both technical and non-technical events which means that it is a fun extravaganza for all the tech maniacs as well as the non-tech mob around the corner looking for opportunities and learnings. It was started in the year 2010 and every year thereafter, different sets of events were organised by the departmental council to instil an element of competition in technology; making it an adventurous ride of coding, technical tools, quizzes, brainstorming games and ideas organised by students."
    str2 = "For the first time in 11 years, Tech Melange was conducted online which resulted in an overwhelming participation from students all over India. It brings together tech-enthusiasts, coders and gamers. Winners are also awarded with lucrative cash prizes, coupons and certificates. Ite is acquainted to the masses by the mingled effort of  the faculty and students."
    str3 ="To maintain the legacy, we have some exciting events this year as well such as Ideathon, Brain Wreck, E - tambola, Cyber hustle, Whiz Quiz and Hardcode. This gives students a golden opportunity to showcase their talent, innovation, creativity and technicality. Students of various renowned universities and colleges(Delhi University, JNU, IP University, IT, Amity, IIIT-D, Jamia Milia etc.) participate in this mass endeavour."
    str4="Our aim is to enhance the intellectual awareness and development of students. The fest adopts a highly participative and interactive approach with a strong emphasis on ‘Learning by Doing’ and is successful in quenching the thirst of today’s well aware techno youth all around."
    
    return render(request, 'index.html', {'stg': str, 'stg1': str1, 'stg2': str2,'stg3':str3 , 'stg4': str4,'a':a})
