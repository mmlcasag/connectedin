from django.db import models

class Perfil(models.Model):
    
    nome = models.CharField(max_length=80, null=False)
    email = models.CharField(max_length=50, null=False)
    telefone = models.CharField(max_length=25, null=True)
    nome_empresa = models.CharField(max_length=80, null=True)
    contatos = models.ManyToManyField('self')
    
    def convidar(self, perfil_convidado):
    	convite = Convite(solicitante=self, convidado=perfil_convidado)
    	convite.save()
    
class Convite(models.Model):

	solicitante = models.ForeignKey(Perfil, related_name="convites_feitos")
	convidado = models.ForeignKey(Perfil, related_name="convites_recebidos")

	def aceitar(self):
		self.convidado.contatos.add(self.solicitante)
		self.solicitante.contatos.add(self.convidado)
		self.delete()