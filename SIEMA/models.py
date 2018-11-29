"""
SIEMA models.
"""
from django.db.models import fields

from opal import models

"""
Core Opal models - these inherit from the abstract data models in
opal.models but can be customised here with extra / altered fields.
"""

class Demographics(models.Demographics):
    first_name = fields.CharField(max_length=255, blank=True, verbose_name=("Nombre"))
    surname = fields.CharField(max_length=255, blank=True, verbose_name=("Apellido"))
    date_of_birth = fields.DateField(verbose_name=("Fecha de nacimiento"))
    #falta traducir sexo :( solo se puede por el momento en los archivos core de Opal
    #falta traducir grupo etnico :( solo se puede por el momento en los archivos core de Opal
    
    pass
class Location(models.Location): 
    category = fields.CharField(max_length=255, blank=True, verbose_name=("Categoria"))
    hospital = fields.CharField(max_length=255, blank=True, verbose_name=("Hospital"))
    ward = fields.CharField(max_length=255, blank=True, verbose_name=("Sala"))
    bed = fields.CharField(max_length=255, blank=True, verbose_name=("Cama"))
    pass
class Diagnosis(models.Diagnosis): 
    #falta traducir condition :( solo se puede por el momento en los archivos core de Opal
    details = fields.CharField(max_length=255, blank=True, verbose_name=("Detalles"))
    date_of_diagnosis = fields.DateField(verbose_name=("Fecha de diagnostico"))
    pass
class PastMedicalHistory(models.PastMedicalHistory): 
    #falta traducir condition :( solo se puede por el momento en los archivos core de Opal
    year = fields.CharField(max_length=255, blank=True, verbose_name=("Anio"))
    details = fields.CharField(max_length=255, blank=True, verbose_name=("Detalles"))
    pass
class Treatment(models.Treatment): 
    #falta traducir drug :( solo se puede por el momento en los archivos core de Opal
    dose = fields.CharField(max_length=255, blank=True, verbose_name=("Dosis"))
    #falta traducir route :( solo se puede por el momento en los archivos core de Opal
    start_date = fields.DateField(verbose_name=("Fecha de Inicio"))
    end_date = fields.DateField(verbose_name=("Fecha de Fin"))
    #falta traducir frequency :( solo se puede por el momento en los archivos core de Opal
    pass
#De aqui hacia abajo ya no se neceita para el demo
class Allergies(models.Allergies): pass
class Investigation(models.Investigation): pass
class SymptomComplex(models.SymptomComplex): pass
class PatientConsultation(models.PatientConsultation): pass

# we commonly need a referral route, ie how the patient
# came to the service, but not always.
# class ReferralRoute(models.ReferralRoute): pass

"""
End Opal core models
"""