from fastmcp import FastMCP
mcp=FastMCP(name='demo remote server')

@mcp.tool()
def calculator(num1: float, num2: float, operator: str) -> float:
    """Perform basic arithmetic operations on two numbers.

    Args:
        num1: The first number.
        num2: The second number.
        operator: The operation to perform (+, -, *, /).
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Invalid operator. Use +, -, *, or /.")

if __name__=="__main__":
    mcp.run(transport='http',host='0.0.0.0',port=8000)