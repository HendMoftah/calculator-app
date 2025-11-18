class CalculatorEngine:
    """Handles the calculator logic and operations"""
    
    def __init__(self):
        self.current_input = "0"
        self.previous_input = ""
        self.operator = ""
        self.should_reset_input = False
    
    def input_digit(self, digit: str):
        """Handle digit input"""
        if self.current_input == "0" or self.should_reset_input:
            self.current_input = digit
            self.should_reset_input = False
        else:
            self.current_input += digit
    
    def input_decimal(self):
        """Handle decimal point input"""
        if self.should_reset_input:
            self.current_input = "0."
            self.should_reset_input = False
        elif "." not in self.current_input:
            self.current_input += "."
    
    def set_operator(self, op: str):
        """Set the operator for calculation"""
        if self.operator and not self.should_reset_input:
            self.calculate()
        
        self.previous_input = self.current_input
        self.operator = op
        self.should_reset_input = True
    
    def calculate(self):
        """Perform the calculation"""
        if not self.operator or not self.previous_input:
            return
        
        try:
            prev = float(self.previous_input)
            current = float(self.current_input)
            
            if self.operator == "+":
                result = prev + current
            elif self.operator == "-":
                result = prev - current
            elif self.operator == "×":
                result = prev * current
            elif self.operator == "÷":
                if current == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = prev / current
            else:
                return
            
            self.current_input = self._format_result(result)
            self.previous_input = ""
            self.operator = ""
            self.should_reset_input = True
            
        except (ValueError, ZeroDivisionError) as e:
            self.current_input = "Error"
            self.should_reset_input = True
    
    def clear(self):
        """Clear the calculator"""
        self.current_input = "0"
        self.previous_input = ""
        self.operator = ""
        self.should_reset_input = False
    
    def clear_entry(self):
        """Clear current entry"""
        self.current_input = "0"
        self.should_reset_input = False
    
    def percentage(self):
        """Convert current input to percentage"""
        try:
            value = float(self.current_input) / 100
            self.current_input = self._format_result(value)
            self.should_reset_input = True
        except ValueError:
            self.current_input = "Error"
            self.should_reset_input = True
    
    def toggle_sign(self):
        """Toggle between positive and negative"""
        if self.current_input and self.current_input != "0":
            if self.current_input.startswith("-"):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
    
    def _format_result(self, result: float) -> str:
        """Format the result for display"""
        if result.is_integer():
            return str(int(result))
        else:
            # Limit decimal places to avoid floating point precision issues
            return f"{result:.10g}"
    
    def get_display(self) -> str:
        """Get the current display value"""
        return self.current_input