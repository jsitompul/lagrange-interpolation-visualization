import numpy as np  # Import NumPy library for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
from matplotlib.animation import FuncAnimation  # Import FuncAnimation for animation
from lagrange import lagrange_interpolation, build_polynomial_string  # Import functions from lagrange.py

# Function to input data points from the user
def input_data():
    n = int(input("Enter the number of data points: "))  # Get number of data points from user
    x_data = []  # Initialize list for x data
    y_data = []  # Initialize list for y data
    for j in range(n):  # Loop through each data point with index j
        x = float(input(f"Enter x[{j+1}]: "))  # Get x value from user
        y = float(input(f"Enter y[{j+1}]: "))  # Get y value from user
        x_data.append(x)  # Append x value to x_data
        y_data.append(y)  # Append y value to y_data
    return np.array(x_data), np.array(y_data)  # Return x_data and y_data as NumPy arrays

# Get input data
x_data, y_data = input_data()  # Get x_data and y_data from user input

# Check if the sizes of x_data and y_data are the same
if len(x_data) != len(y_data):  # If lengths are not the same, raise an error
    raise ValueError("x_data and y_data must be of the same size")  # Raise ValueError

# Define the range for plotting
x_range = np.linspace(np.min(x_data) - 1, np.max(x_data) + 1, 400)  # Define x range for plotting

# Plotting setup
fig, ax = plt.subplots()  # Create a figure and axis for plotting
ax.set_xlim(np.min(x_data) - 1, np.max(x_data) + 1)  # Set x limits of the plot
ax.set_ylim(np.min(y_data) - 1, np.max(y_data) + 1)  # Set y limits of the plot
line, = ax.plot([], [], lw=2)  # Initialize line object for the plot

# Initialize variable to store the final polynomial result and terms
final_polynomial = None  # Initialize final_polynomial to None
polynomial_terms = None  # Initialize polynomial_terms to None

# Function to update the plot for animation
interpolator = lagrange_interpolation(x_data, y_data, x_range)  # Get interpolator generator
def update(frame):
    global final_polynomial, polynomial_terms  # Declare global variables
    if len(frame) == 2:  # Check if frame has 2 elements
        P, i = frame  # Unpack polynomial P and index i from frame
    else:
        P, i, polynomial_terms = frame  # Unpack polynomial P, index i, and polynomial_terms from frame
        final_polynomial = P  # Update final_polynomial with P
    line.set_data(x_range, P)  # Update line data with new polynomial values
    ax.set_title(f'Lagrange Interpolating Polynomial')  # Update plot title with current step
    return line,  # Return the line object

# Animation setup
ani = FuncAnimation(fig, update, frames=interpolator, interval=50, blit=True, repeat=False)  # Set up animation

plt.title('Lagrange Interpolating Polynomial')  # Set plot title
plt.scatter(x_data, y_data, color='red', label='Data Points')  # Plot data points as red dots
plt.legend()  # Add legend to the plot
plt.xlabel('X')  # Set x-axis label
plt.ylabel('Y')  # Set y-axis label

plt.show()  # Show the plot

# Print the final polynomial result
if polynomial_terms is not None:  # If polynomial_terms is not None
    polynomial_str = build_polynomial_string(polynomial_terms)  # Build polynomial string
    print("Final Lagrange Interpolating Polynomial:\nP(x)= " + polynomial_str)  # Print the polynomial string)  # Print final polynomial label and string
    
