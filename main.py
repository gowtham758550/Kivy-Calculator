import kivy
kivy.require("1.9.0")
 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
 
class CalcGridLayout(GridLayout):

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                stripped = lambda str, symbol : str.strip(symbol)
                if self.display.text.endswith('+'):
                	self.display.text = str(eval(stripped(calculation, '+')))
                elif self.display.text.endswith('-'):
                	self.display.text = str(eval(right_stripped(calculation, '-')))
                elif self.display.text.startswith('*') or self.display.text.endswith('*'):
                	self.display.text = str(eval(stripped(calculation, '*')))
                elif self.display.text.startswith('/') or self.display.text.endswith('/'):
                	self.display.text = str(eval(stripped(calculation, '/')))
                                
                
    def delete(self, text):
                text = str(text)
                n = len(text) - 1
                self.display.text = text[0:n]
                
    def stop(self):
    	exit(1)

 
class CalculatorApp(App):
 
    def build(self):
        return CalcGridLayout()
 
calcApp = CalculatorApp()
calcApp.run()
 
