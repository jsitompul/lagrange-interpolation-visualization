import numpy as np  # Import NumPy library for numerical operations

# Function to compute the Lagrange basis polynomial L_i
def lagrange_basis(x_vals, i, x):
    product = 1  # Initialize product to 1
    for j, x_j in enumerate(x_vals):  # Loop through x_vals with index j
        if j != i:  # Skip the current index i
            product *= (x - x_j) / (x_vals[i] - x_j)  # Update product for L_i
    return product  # Return the Lagrange basis polynomial L_i

# Function to compute the full Lagrange polynomial incrementally
def lagrange_interpolation(x_vals, y_vals, x):
    n = len(x_vals)  # Number of data points
    P = np.zeros_like(x)  # Initialize polynomial P to zeros
    polynomial_terms = []  # Initialize list to store polynomial terms
    for i in range(n):  # Loop through each data point with index i
        L_i = lagrange_basis(x_vals, i, x)  # Compute Lagrange basis polynomial L_i
        polynomial_terms.append((y_vals[i], x_vals, i))  # Append term to polynomial_terms
        for alpha in np.linspace(0, 1, 100):  # Smoother transition using alpha
            yield P + alpha * y_vals[i] * L_i, i  # Yield intermediate polynomial and index
        P += y_vals[i] * L_i  # Update polynomial P with term for current index i
    yield P, n, polynomial_terms  # Yield final polynomial, number of terms, and polynomial_terms

# Function to build the polynomial equation string using SymPy for simplification
def build_polynomial_string(terms):
    import sympy as sp  # Import SymPy for symbolic computation
    x = sp.Symbol('x')  # Define symbolic variable x
    polynomial = 0  # Initialize polynomial to 0
    for coef, x_vals, i in terms:  # Loop through each term
        term = coef  # Initialize term with coefficient
        for j, x_j in enumerate(x_vals):  # Loop through x_vals with index j
            if j != i:  # Skip the current index i
                term *= (x - x_j) / (x_vals[i] - x_j)  # Update term for L_i
        polynomial += term  # Add term to polynomial
    simplified_polynomial = sp.simplify(polynomial)  # Simplify polynomial using SymPy
    return str(simplified_polynomial)  # Return simplified polynomial as a string
