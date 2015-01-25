# DateTime
import datetime

# django
from django.db import models
from django.contrib.contenttypes import generic

# eav
from eav.models import BaseChoice, BaseEntity, BaseSchema, BaseAttribute

# Extra Imports
from patient.utils import get_upload_file_path
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Register(models.Model):
    DOCTOR_CHOICE = (
        ('Kumari', 'kumari'),
        ('Shalini', 'shalini'),
    )
    firstname = models.CharField(_('First Name'), max_length=50)
    lastname = models.CharField(_('Last Name'), max_length=50)
    age = models.CharField(_('Age'), max_length=20)
    contactno = models.CharField(_('Contact No.'), max_length=10)
    date = models.DateField(_('Date'), default=datetime.date.today())
    doctor = models.CharField(_('Doctor'), choices=DOCTOR_CHOICE, max_length=25)
    picture = models.ImageField(_('Image'), upload_to=get_upload_file_path)

    def __unicode__(self):
        return self.firstname

class Attribute(BaseAttribute):
    schema = models.ForeignKey("Schema", related_name='attrs')
    choice = models.ForeignKey("Choice", blank=True, null=True)
    
class Disease(BaseEntity):
    patient = models.ForeignKey(Register)
    symptom = models.CharField(_('Disease Symptom'), max_length=50)
    doctor = models.CharField(_('Doctor Consulted'), max_length=50)
    prescription = models.CharField(_('Prescription'), max_length=50)
    report = models.FileField(_('Report Attachment'), upload_to=get_upload_file_path)
    disease = models.CharField(_('Detected Disease'), max_length=50)
    cured = models.BooleanField()
    attrs = generic.GenericRelation(Attribute, object_id_field='entity_id',
                                    content_type_field='entity_type')
    @classmethod
    def get_schemata_for_model(self):
        return Schema.objects.all()

    def __unicode__(self):
        return self.title


class Schema(BaseSchema):
    pass


class Choice(BaseChoice):
    schema = models.ForeignKey(Schema, related_name='choices')


