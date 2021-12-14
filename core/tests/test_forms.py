from django.test import TestCase

from core.forms import ContatoForm

class ContatoFormTestCase(TestCase):

	def setUp(self):
		self.nome = 'Nome'
		self.email = 'contato@teste.com'
		self.mensagem = 'Uma mensagem qualquer'
		self.assunto = 'Assunto'

		self.data = {
			'nome': self.nome,
			'email': self.email,
			'mensagem': self.mensagem,
			'assunto': self.assunto
		}

		self.form = ContatoForm(data=self.data)

	def test_send_mail(self):
		form1 = ContatoForm(self.data)
		form1.is_valid()
		res1 = form1.send_mail()

		form2 = self.form
		form2.is_valid()
		res2 = form2.send_mail()
		self.assertEqual(res1, res2)