import matplotlib.pyplot as plt

# Sample data
x_axis = ['1800', '1801', '1802', '1803', '1804']
y_axis_my_country = [28.2, 28.4, 28.6, 28.8, 29.0]  # Example data for Brazil
y_axis_other_country = [27.0, 27.2, 27.4, 27.6, 27.8]  # Example data for Angola

# Country names
my_country = "Brazil"
other_country = "Angola"

# Plotting both countries
plt.plot(x_axis, y_axis_my_country, label=my_country, marker='o')  # Brazil
plt.plot(x_axis, y_axis_other_country, label=other_country, marker='o')  # Angola

# Set title and labels
plt.title("Populations Projection")
plt.xlabel("Year")
plt.ylabel("Population")

# Add legend
plt.legend()  # This should work

# Show plot
# plt.tight_layout()
plt.show()
