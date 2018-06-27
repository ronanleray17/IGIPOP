from django.contrib import admin
from django.utils.text import Truncator
from blog.models import T_IG, T_statut, T_document

# Register your models here.
class IGAdmin(admin.ModelAdmin):
    list_display   = ('ID_IG', 'statut','ouvrages', 'date_debut', 'date_fin', 'apercu_resume')
    list_filter    = ('postes','date_debut','ID_IG','statut',)
    date_hierarchy = 'date_debut'
    ordering       = ('date_debut', )
    search_fields  = ('postes', 'ouvrages', 'resume')
    
    fieldsets = (
        ('Général (SPORT)', {
            'classes': ['collapse', ],
            'fields' : ('ID_IG', 'date_debut', 'date_fin', 'ouvrages', 'postes')
        }),
        ('Etude : ', {
            'fields': ('resume','statut','details',)
        }),

    )

    def apercu_resume(self, IG):
        """ 
        Retourne les 40 premiers caractères du contenu de l'article, 
        suivi de points de suspension si le texte est plus long. 

        On pourrait le coder nous même, mais Django fournit déjà la 
        fonction qui le fait pour nous !
        """
        return Truncator(IG.resume).chars(40, truncate='...')

    # En-tête de notre colonne
    apercu_resume.short_description = 'Aperçu du résumé'

admin.site.register(T_IG, IGAdmin)
admin.site.register(T_statut)
admin.site.register(T_document)

