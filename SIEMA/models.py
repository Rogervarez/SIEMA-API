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
class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Treatment(models.Treatment): pass
class Investigation(models.Investigation): pass
class SymptomComplex(models.SymptomComplex): pass
class PatientConsultation(models.PatientConsultation): pass

# we commonly need a referral route, ie how the patient
# came to the service, but not always.
# class ReferralRoute(models.ReferralRoute): pass

"""
End Opal core models
"""