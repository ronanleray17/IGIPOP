from django.db import models
from django.views.generic import TemplateView
from django.utils import timezone
"""Pour créer une nouvelle table, lancer python3 manage.py makemigrations puis migrate"""

class T_IG(models.Model):
    ID_IG = models.CharField(max_length=20)
    postes = models.CharField(max_length=255,null=True)
    ouvrages = models.TextField(null=True)
    date_debut = models.DateTimeField(default=timezone.now, verbose_name="Date début IG")
    date_fin = models.DateTimeField(default=timezone.now,       verbose_name="Date fin IG")
    resume = models.TextField(null=True)
    details = models.TextField(null=True)
    statut = models.ForeignKey('T_statut', on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = "Détails IG et étude"
        ordering = ['date_debut']
                        
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return "[{0}] {1}".format(self.ID_IG, self.ouvrages)
   

class T_statut(models.Model):
    statut = models.CharField(max_length=20)
    
    def __str__(self):
        return self.statut
    
def renommage(instance, nom_fichier):
        return "static/docs/PJ/" + "{}-{}".format(instance.IG.ID_IG, nom_fichier)
    
class T_document(models.Model):
    IG = models.ForeignKey('T_IG', on_delete=models.CASCADE)
    nom = models.CharField(max_length=100, null=True)
    dateUp = models.DateTimeField(default=timezone.now, verbose_name="Date upload")
    uploader = models.CharField(max_length=100, null=True)
    doc = models.FileField(upload_to=renommage)
    
    class Meta:
        verbose_name = "Pièces jointes"
        ordering = ['dateUp']
    
    def __str__(self):
        return "[{0}] {1}".format(self.IG, self.nom)

class FAQView(TemplateView):
   template_name = "blog/faq.html"  # chemin vers le template à afficher
