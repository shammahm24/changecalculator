#!/usr/bin/python-3
import sys
import os

class changeCalculator:
	def __init__(self):
		self.amount

	def askAmount(self):
		self.amount=float(input("Enter amount to be changed :$"))
		return self.amount

	def calculate(self):
		cents=int(self.amount*100)
		quarters=int((cents/25))
		dimes=int(((cents%25)/10))
		nickels=int((((cents%25)%10)/5))
		pennies=int((((cents%25)%10)%5))
		print("The change is:.....................\n \n"+
			"\t"+str(quarters)+"\tquaters \n"+
			"\t"+str(dimes)+"\t dimes \n"+
			"\t"+str(nickels)+"\t nickels \n"+
			"\t"+str(pennies)+"\tpennies  \n\n"+
			"**********************\n\n\n")

	def main(self):
		
		while True:
			self.askAmount(self)
			self.calculate(self)
cal=changeCalculator
cal.main(cal)
