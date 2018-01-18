from django.shortcuts import render

from about.forms import ContactForm

# Create your views here.
def get_index(request):
    return render(request, 'about.html')

def get_contact(request):
    
    form_class = ContactForm
    
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            template=get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)
            
            subject = 'Thanks for getting in touch!'
            message = 'Thank you for contacting Urban Surf. We will get back to you as soon as we can'
            from_email = settings.EMAIL_HOST_USER
            to_email = [contact_email]

            send_mail(subject,message,from_email,to_email,fail_silently=True)

            email = EmailMessage(
                "New contact form message",
                content,
                "Your website" +'',
                ['ngonneke@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.success(request, 'We have recieved your email & will get back to you as soon as possible!')
            return redirect('index')

    return render(request, 'contact.html', {
        'form': form_class,
    })













