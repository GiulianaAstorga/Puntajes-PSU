# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Colegio(models.Model):
    unidad_educativa = models.CharField(db_column='UNIDAD_EDUCATIVA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rama_educacional = models.CharField(db_column='RAMA_EDUCACIONAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dep = models.CharField(db_column='DEP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rbd = models.IntegerField(db_column='RBD', primary_key=True, blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    
    class Meta:
        managed = False
        db_table = 'COLEGIO'
    def __str__(self):
        return self.unidad_educativa
    

class Ciencias(models.Model):
    colegio_c = models.OneToOneField('Colegio', db_column='id',primary_key=True, blank=True, null=False)
    n_ccs = models.IntegerField(db_column='N_CCS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    p_ccs = models.FloatField(db_column='P_CCS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    max_ccs = models.FloatField(db_column='MAX_CCS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    min_ccs = models.FloatField(db_column='MIN_CCS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    
    
    class Meta:
        managed = False
        db_table = 'CIENCIAS'

     

class Historia(models.Model):
    colegio_h = models.OneToOneField(Colegio, db_column='id',primary_key=True, blank=True, null=False)
    n_his = models.IntegerField(db_column='N_HIS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    p_his = models.FloatField(db_column='P_HIS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    max_his = models.FloatField(db_column='MAX_HIS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    min_his = models.FloatField(db_column='MIN_HIS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    

    class Meta:
        managed = False
        db_table = 'HISTORIA'


class Lenguaje(models.Model):
    colegio_l = models.OneToOneField(Colegio, db_column='id',primary_key=True, blank=True, null=False)
    n_len = models.IntegerField(db_column='N_LEN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    p_len = models.FloatField(db_column='P_LEN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    max_len = models.FloatField(db_column='MAX_LEN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    min_len = models.FloatField(db_column='MIN_LEN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    

    class Meta:
        managed = False
        db_table = 'LENGUAJE'


class LenMat(models.Model):
    colegio_lm = models.OneToOneField(Colegio, db_column='id', primary_key=True, blank=True, null=False)
    n_lm = models.IntegerField(db_column='N_LM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    p_lm = models.FloatField(db_column='P_LM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    max_lm = models.FloatField(db_column='MAX_LM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    min_lm = models.FloatField(db_column='MIN_LM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    

    class Meta:
        managed = False
        db_table = 'LEN_MAT'


class Localidad(models.Model):
    colegio_lc = models.OneToOneField(Colegio, db_column='id',primary_key=True, blank=True, null=False)
    region = models.IntegerField(db_column='REGION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prov = models.CharField(db_column='PROV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comuna = models.CharField(db_column='COMUNA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    

    class Meta:
        managed = False
        db_table = 'LOCALIDAD'


class Matematicas(models.Model):
    colegio_m= models.OneToOneField(Colegio, db_column='id',primary_key=True, blank=True, null=False)
    n_mat = models.IntegerField(db_column='N_MAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    p_mat = models.FloatField(db_column='P_MAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    max_mat = models.FloatField(db_column='MAX_MAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    min_mat = models.FloatField(db_column='MIN_MAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    

    class Meta:
        managed = False
        db_table = 'MATEMATICAS'


class PromedioGeneral(models.Model):
    colegio_pg= models.OneToOneField(Colegio, db_column='id',primary_key=True, blank=True, null=False)
    n_pg = models.IntegerField(db_column='N_PG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    p_pg = models.FloatField(db_column='P_PG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    max_pg = models.FloatField(db_column='MAX_PG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    min_pg = models.FloatField(db_column='MIN_PG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    colegio_pg= models.OneToOneField(Colegio, db_column='id',primary_key=True, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'PROMEDIO_GENERAL'


class Ranking(models.Model):
    colegio_rk = models.OneToOneField(Colegio, db_column='id',primary_key=True, blank=True, null=False)
    n_rkg = models.IntegerField(db_column='N_RKG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    p_rkg = models.FloatField(db_column='P_RKG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    max_rkg = models.FloatField(db_column='MAX_RKG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    min_rkg = models.FloatField(db_column='MIN_RKG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    

    class Meta:
        managed = False
        db_table = 'RANKING'
