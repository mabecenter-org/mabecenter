# Copyright (c) 2024, Dante Devenir and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe


class Card(Document):
	
	def autoname(self):
		# Tomamos el nombre y los últimos 4 dígitos del número de tarjeta
		formatted_number = '-'.join([self.card_number[i:i+4] for i in range(0, len(self.card_number), 4)])

		# Generamos el nuevo nombre del Doctype con el formato deseado
		self.name = formatted_number
