import sys
import os
# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nicegui import ui
from src.calculator.calculator_engine import CalculatorEngine

class CalculatorApp:
    def __init__(self):
        self.calc = CalculatorEngine()
        self.create_ui()
    
    def create_ui(self):
        """Create the calculator UI"""
        # Main container with calculator styling
        with ui.card().classes('w-80 mx-auto mt-8 shadow-2xl rounded-2xl overflow-hidden bg-gray-900'):
            
            # Display area
            with ui.card().classes('w-full p-4 bg-gray-800 rounded-t-2xl'):
                # Expression display (smaller, above main display)
                with ui.row().classes('w-full justify-end h-6'):
                    ui.label().bind_text_from(self.calc, 'previous_input').classes('text-gray-400 text-sm')
                    ui.label().bind_text_from(self.calc, 'operator').classes('text-gray-400 text-sm')
                
                # Main display
                ui.label().bind_text_from(self.calc, 'current_input').classes(
                    'w-full text-right text-3xl font-mono font-bold text-white'
                ).style('min-height: 60px; line-height: 60px;')
            
            # Button grid
            with ui.grid(columns=4).classes('w-full gap-2 p-4 bg-gray-900'):
                # Row 1
                self.create_button('C', 'clear', 'bg-red-500 hover:bg-red-600 text-white')
                self.create_button('±', 'toggle_sign', 'bg-gray-600 hover:bg-gray-700 text-white')
                self.create_button('%', 'percentage', 'bg-gray-600 hover:bg-gray-700 text-white')
                self.create_button('÷', lambda: self.set_operator('÷'), 'bg-orange-500 hover:bg-orange-600 text-white')
                
                # Row 2
                self.create_button('7', lambda: self.input_digit('7'), 'bg-gray-700 hover:bg-gray-600 text-white')
                self.create_button('8', lambda: self.input_digit('8'), 'bg-gray-700 hover:bg-gray-600 text-white')
                self.create_button('9', lambda: self.input_digit('9'), 'bg-gray-700 hover:bg-gray-600 text-white')
                self.create_button('×', lambda: self.set_operator('×'), 'bg-orange-500 hover:bg-orange-600 text-white')
                
                # Row 3
                self.create_button('4', lambda: self.input_digit('4'), 'bg-gray-700 hover:bg-gray-600 text-white')
                self.create_button('5', lambda: self.input_digit('5'), 'bg-gray-700 hover:bg-gray-600 text-white')
                self.create_button('6', lambda: self.input_digit('6'), 'bg-gray-700 hover:bg-gray-600 text-white')
                self.create_button('-', lambda: self.set_operator('-'), 'bg-orange-500 hover:bg-orange-600 text-white')
                
                # Row 4
                self.create_button('1', lambda: self.input_digit('1'), 'bg-gray-700 hover:bg-gray-600 text-white')
                self.create_button('2', lambda: self.input_digit('2'), 'bg-gray-700 hover:bg-gray-600 text-white')
                self.create_button('3', lambda: self.input_digit('3'), 'bg-gray-700 hover:bg-gray-600 text-white')
                self.create_button('+', lambda: self.set_operator('+'), 'bg-orange-500 hover:bg-orange-600 text-white')
                
                # Row 5
                self.create_button('0', lambda: self.input_digit('0'), 'bg-gray-700 hover:bg-gray-600 text-white col-span-2')
                self.create_button('.', 'input_decimal', 'bg-gray-700 hover:bg-gray-600 text-white')
                self.create_button('=', 'calculate', 'bg-orange-500 hover:bg-orange-600 text-white')
    
    def create_button(self, label: str, action, classes: str):
        """Create a calculator button"""
        if isinstance(action, str):
            # If action is a string, it's a method name
            method = getattr(self.calc, action)
            ui.button(label, on_click=method).classes(f'h-16 text-xl font-bold rounded-xl {classes}')
        else:
            # If action is a function
            ui.button(label, on_click=action).classes(f'h-16 text-xl font-bold rounded-xl {classes}')
    
    def input_digit(self, digit: str):
        """Handle digit input"""
        self.calc.input_digit(digit)
    
    def set_operator(self, op: str):
        """Set operator"""
        self.calc.set_operator(op)

def main():
    """Main function to run the calculator app"""
    app = CalculatorApp()
    
    # Configure and run the app
    ui.run(
        title='Modern Calculator',
        host='0.0.0.0',
        port=8080,
        reload=False,
        show=True,
        dark=True  # Enable dark mode
    )

if __name__ == "__main__":
    main()