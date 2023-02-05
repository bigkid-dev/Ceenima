
from django.shortcuts import render
from django.views.generic.base import RedirectView

from django.conf import settings
# generate pdf and qrcode
from fpdf import FPDF
import qrcode

# miscellaeneus
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from .models import Shows, Upcoming_Movies, Cenima_Show, New_movies
from .serializers import ShowSerializer




from django.shortcuts import render, redirect
from .forms import ShowForm
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.templatetags.static import static

# authentication
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# to handle the mail


# messages
from django.contrib import messages
from django.contrib.auth.decorators import login_required


import os


# transaction id generator
import random
import string





class ShowView(generics.CreateAPIView):
  queryset = Shows.objects.all()
  serializer_class = ShowSerializer


def generate_transaction_id():
  length = 9
  while (True):
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    break
  return code


# Create your views here.
def generateCode():
  #Creating a QRCode object ouserf the size specified by the 
    qr = qrcode.QRCode(
            version = 5,
            box_size = 3,
            border = 5)

    img = qrcode.make('Some data here')
    type(img)  # qrcode.image.pil.PilImage
    img.save("some_file.png")
 

generateCode()


pdf_w=210
pdf_h=297

class PDF(FPDF):
    pass


def create_pdf(movie_title, location, ticket_id, name):
  pdf = PDF(orientation='P', unit='mm', format='A4')
  pdf.add_page()
  pdf.rect(8.0, 8.0, 200.0,287.0)
  # pdf.rect(5.1, pdf_h/2, 200.0, 287.0)

  pdf.set_xy(0.0,0.0)
  pdf.set_font('Arial', 'B', 16)
  pdf.set_text_color(220, 50, 50)

  pdf.multi_cell(0, 8, txt="   CEENIMA")
  pdf.image('some_file.png',  link='', type='', w=500/5, h=450/5)

  pdf.set_text_color(14, 14, 14)
  pdf.set_font('Arial', 'B', 10)
  pdf.multi_cell(0, 20, txt="   CEENIMA")
  pdf.set_font('Arial', 'B', 14)
  pdf.multi_cell(0, 20, movie_title)
  pdf.set_font('Arial', 'B', 11)
  pdf.multi_cell(0, 20, 'YOUR Movie ticket id:   ' + ticket_id + '\n' + 'Name:  ' + name )

  folder = os.path.join(settings.FILES_URL, name)
  user_name = str(name)
  ext = '.pdf'
  if os.path.exists(folder):    
    folder = os.path.join(folder, f'{user_name}{ext}')
    pdf.output( folder ,'f')

  else:
    os.makedirs(folder)
    folder = os.path.join(folder, f'{user_name}{ext}')
    pdf.output( folder ,'f')

  name = "Ireoluwa"
  size = 20
#Function to generate the QR code and save it



class ModelCreateView(CreateView):
    model = Shows
    fields = [
      "title","description","summary","link","image_link","time_showing","second_time_showing","third_time_showinng",
      "fourth_time_showing"
    ]
    
    success_url = "List"



class ShowsListView(ListView):
    model = Shows
    template_name = "list.html"

    def my_view(self, request):
      context = Shows.object_all().values()
      args = {'context': context}
      return render(request, 'list.html', args) 


def homepage(request):
  id = Cenima_Show.objects.count()
  one = Cenima_Show.objects.filter(id=id)
  two = Cenima_Show.objects.filter(id=id-1)
  three = Cenima_Show.objects.filter(id=id-2)
  four = Cenima_Show.objects.filter(id=id-3)
  
  
  return render(request, 'index.html', { 'one':one, 'two':two, 'three':three, 'four':four}) 






def show_list(request):
  if request.method == "POST":
    form = ShowForm(request.POST)

    if form.is_valid():
      try:
        form.save()
        return redirect('/Create')
      except:
        pass

  else:
    form = ShowForm()
    print("error")

  return render(request,'forms.html',{'form':form})


def display(request):
  shows = ShowForm.objects.all()

  return render(request, '',{'shows':shows})


def all_shows(request):
  show = request.GET.get('id')
  show = Cenima_Show.objects.filter(id=show)

  if request.method == "POST":
    return redirect('pay')

  return render(request,'test.html', {'show':show})


# class NewShowsListView(ListView):
#     model = Cenima_Show
#     template_name = "show.html"
@login_required
def NewShowsListView(request):
  show = Cenima_Show.objects.all()
  
  # context = Shows.object_all().values()
  if User.is_authenticated:
    show = Cenima_Show.objects.all()
    args = {'show':show}
    print(request.user)
    return render(request, 'show.html', {'show':show})
  else:
    return render(request, 'show.html', {'show':show})


def navbar_view(request):
  return render(request, 'cenima/navbar.html')


def footer_view(request):
  return render(request, 'cenima/footer.html')



class Cenima_Show_view(CreateView, RedirectView):
  model = Cenima_Show
  template = "cenima/cenima_show_form.html"
  fields = ["title","description","summary","link","image_link","time_showing","second_time_showing","third_time_showing",
      "fourth_time_showing", "location", "price", "date_showing", "second_date_showing", "third_date_showing", "fourth_date_showing"]
  success_url = "Lists"
  template_name = "cenima_show"
  
  def my_view(self, request):
    context = Shows.object_all().values()
    args = {'context': context}
    return render(request,'cenima_show.html', args )



class Upcoming_Movies_View(CreateView):
  model = Upcoming_Movies
  template_name = "cenima/upcoming_movies_form.html"
  fields = ['upcoming_pic']

  def my_view():
    context = Shows.object_all().values()
    args = {'context': context}
    return render(request, 'upcoming_movies_form.html', args)


class New_Movies_View(CreateView):
  model = New_movies
  template_name = "cenima/new_movies_form.html"
  fields = ['new_pic']
  success_url = "list.html"

  def my_view():
    context = Shows.object_all().values()
    args = {'context': context}
    return render(request, 'new_movies_form.html', args)



def email_handler(reciever_email):
  subject = 'Subject'
  html_message = render_to_string('cenima/email_template.html', {'context': 'values'})
  plain_message = strip_tags(html_message)
  from_email = 'settings.EMAIL_HOST_USER'
  to = reciever_email

  mail.send_mail(subject, plain_message, from_email, [to], html_message )


@login_required
def payments(request):
  pay = request.GET.get('id')
  pay = Cenima_Show.objects.filter(id=pay)

  if request.method == "POST":
    for pay in pay:
      movie_title = pay.title
      location = pay.location
      ticket_id = generate_transaction_id()
      name = request.user.username
      generateCode()
      create_pdf(movie_title, location, ticket_id, name)
      

    return render(request,'thank_you.html', {'path': thanks(request)})

  return render(request,'cenima/payments.html', {'pay': pay})



def login_page(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('homepage')

    else:
      messages.info(request, "invalid username or password")
      
  return render(request, 'auth/login.html')



def signup(request):
  if request.method == "POST":
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()
    return redirect('homepage')

  return render(request, 'auth/signup.html')


def about_us_page(request):
  return render(request, 'about-us.html')


def booking_page(request):
  return render(request, 'booking.html')


def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")


def mail_sender():
  message = Mail(from_email='mentalitysounds@gmail.com',to_emails='millenniumbest777@gmail.com',subject='Sending with Twilio SendGrid is Fun',html_content='<strong>and easy to do anywhere, even with Python</strong>')
  try:
      sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
      response = sg.send(message)
      print(response.status_code)
      print(response.body)
      print(response.headers)
  except Exception as e:
      # print(e.message)
      print("ERROR: PC LOAD LETTER")



def signin(request):
  return render(request, 'auth/pre-login.html')



def logout_page(request):
  if request.method == "POST":

    if request.user is not None:
      logout(request)
      return redirect('signup_view')

    else:
      messages.info(request, "invalid username or password")
      
  else:
    return render(request, 'auth/logout.html')


def prelogin(request):
  pay = Cenima_Show.objects.filter(id=3)
  name = request.user.username
  for pay in pay:
    movie_title = pay.title
    location = pay.location
    ticket_id = generate_transaction_id()
  if request.method == "POST":
    
    generateCode()
    create_pdf(movie_title, location, ticket_id, name )
    generateCode()
    return render(request,'thanks', {'path': thanks(request)})
  
  return render(request, 'auth/pre-login.html')

# download page
def thanks(request):
  username = request.user.username
  user_name = str(username)
  ext = '.pdf'
  tag = '/'
  folder = 'files' + f'{tag}{user_name}{tag}' + f'{user_name}{ext}'
  path = static(folder)
  # /static/files/test5.pdf
  print(path)
  # return render (request, 'thank_you.html',{'path': path})
  return path


def page_not_found(request, exception):
  return render(request, '404.html', status=404)