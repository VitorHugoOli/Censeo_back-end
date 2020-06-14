from django.db import models


# Create your models here.
from curso.models import Curso, TopicoSugestaoCurso


class Aluno(models.Model):
    idaluno = models.IntegerField(db_column='idAluno', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=45, blank=True, null=True)
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    login = models.CharField(max_length=45, blank=True, null=True)
    senha = models.CharField(max_length=45)
    matricula = models.CharField(max_length=45)
    xp = models.DecimalField(db_column='XP', max_digits=20, decimal_places=0, blank=True,
                             null=True)  # Field name made lowercase.
    curso_idcurso = models.ForeignKey(Curso, models.DO_NOTHING,
                                      db_column='Curso_idCurso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Aluno'




class Elo(models.Model):
    idelo = models.IntegerField(db_column='idElo', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    aluno_idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='Aluno_idAluno')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Elo'
        unique_together = (('idelo', 'aluno_idaluno'),)

class SugestaoCurso(models.Model):
    idsugestao_curso = models.IntegerField(db_column='idSugestao_Curso', primary_key=True)  # Field name made lowercase.
    sugestao = models.CharField(max_length=45, blank=True, null=True)
    titulo = models.CharField(max_length=45, blank=True, null=True)
    relevancia = models.CharField(max_length=15, blank=True, null=True)
    curso_idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='Curso_idCurso')  # Field name made lowercase.
    topico_sugestao_curso_idtopico_sugestao_curso = models.ForeignKey(TopicoSugestaoCurso, models.DO_NOTHING,
                                                                      db_column='Topico_Sugestao_Curso_idTopico_Sugestao_Curso')  # Field name made lowercase.
    aluno_idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='Aluno_idAluno')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sugestao_Curso'
        unique_together = (
        ('idsugestao_curso', 'curso_idcurso', 'topico_sugestao_curso_idtopico_sugestao_curso', 'aluno_idaluno'),)