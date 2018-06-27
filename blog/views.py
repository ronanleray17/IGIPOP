from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import T_IG, T_statut, T_document
from blog.forms import ContactForm, T_IGForm, importPJ

def home(request):
    lst_IG = T_IG.objects.all
    return render(request, 'index.html',{'liste_IG':lst_IG})

def view_IG(request, id_IG):
    IG = get_object_or_404(T_IG, ID_IG=id_IG)
    PJ = T_document.objects.filter(IG=IG)
    """Vue qui affiche les détails d'une étude selon son numéro d'IG"""
    return render(request, 'detail_IG.html',locals())

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'contact.html', locals())

def edit_IG(request, id_IG):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    IG = get_object_or_404(T_IG, ID_IG=id_IG)
    if request.method == "POST" :
        form = T_IGForm(request.POST, instance=get_object_or_404(T_IG, ID_IG=id_IG))
    else:
        form = T_IGForm(instance = get_object_or_404(T_IG, ID_IG=id_IG))
    #if edit == True:
    
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        form.save()
        saved = True
    else :
        saved = False
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    edit = True
    return render(request, 'edit_IG.html', locals())

def importerPJ(request):
    sauvegarde = False
    form = importPJ(request.POST or None, request.FILES)
    if form.is_valid():
        doc = T_document()
        doc.IG = form.cleaned_data["IG"]
        doc.nom = form.cleaned_data["nom"]
        doc.uploader = form.cleaned_data["uploader"]
        doc.doc = form.cleaned_data["doc"]
        doc.save()
        sauvegarde = True
        
    return render(request, 'ajout_PJ.html', {
        'form' : form,
        'sauvegarde' : sauvegarde
    })
