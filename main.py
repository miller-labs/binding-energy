# Date created: 04/04/2024
# Date modified: 05/04/2024
# Created by: Joel Miller
# This is a project to calculate the binding energy of "n" number of objects for a given geometry.
import math

#######################################################################################################################
# Stage 1

# Define constants
sigma = 3.41e-10  # in meters
epsilon = 1.65e-21  # in joules


#######################################################################################################################
# Stage 2

# create a function to calculate the binding energy of a single object pairing
def binding_energy_calc(r):
    return 4 * epsilon * ((sigma / r) ** 12 - (sigma / r) ** 6)


#######################################################################################################################
# Stage 3
# Define given distances (r, in metres) between the three objects
r1_2 = 4.1e-10  # distance between object 1 and 2
r1_3 = 2e-10  # distance between object 1 and 3
r2_3 = 3.41e-10  # distance between object 2 and 3

distances_list = [r1_2, r1_3, r2_3,r1_3,r1_3, r2_3]  # List of all distances between each of the objects

# Example case
r_example = [6.82e-10]  # in metres
example_u = -1.0e-22  # in Joules


#######################################################################################################################
# Side Note
# A more universal approach would be to have a .txt file containing all distances and importing the file contents
# to a list.
# Or, if you have a list of (x, y) coordinates for all objects, you could then calculate the distances between all
# objects and append these results to a list of distances i.e., r_list.
# For more than three objects, there will be more pairings than there are objects.
# The number of pairings for 'n' objects = n(n-1)/2
# Later, we will create a programme to do this for us
#######################################################################################################################


#######################################################################################################################
# Stage 4
# Calculate the binding energies


def total_binding_energy_calc(distances):  # Function to calculate total binding energy from list of object separations
    binding_energies_list = []  # Initialize empty list to store calculate individual pairwise binding energies

    for r in distances:
        binding_energy = binding_energy_calc(r)  # calculate individual binding energies using custom function
        binding_energies_list.append(binding_energy)

    total_binding_energy = sum(binding_energies_list)

    n_pairings = len(distances)
    if n_pairings <= 1:
        print('There is', n_pairings, 'separation in this list')
        print('The total binding energy of the', n_pairings, 'separation is', total_binding_energy, 'J')
    else:
        print('There are', n_pairings, 'separations in this list')
        print('The total binding energy of the', n_pairings, 'separations is', total_binding_energy, 'J')
    # print('Number of Pairings is ', int(n_pairings))

    # print(n_pairings)
    return total_binding_energy


#######################################################################################################################
# Stage 5
# Run the programme to calculate the total binding energy

total_binding_energy_calc(distances_list)


#######################################################################################################################
# Side note
# If we are given a list with an incorrect number of separations, then our calculation for the total binding energy
# will be incorrect. For instance, 10 objects provides 27 pairings. If we have a list containing 28 pairings,
# then we end up with a non-integer number of objects, which is impossible. We can use this information to include a
# check within our code, that tells us if we have a reasonable number of elements in our list. Of course, it's possible
# that we randomly end up with a list containing a reasonable number of elements; however, this check minimises the
# chance of the code outputting the incorrect result

# Stage 5
# To do this I can take the equation: n_pairings = (n * (n - 1)) / 2, and rearrange for n.
# This gives gives a quadratic equation (n^2 − n − 2 x n_pairings = 0), which can be solved using the quadratic formula.
# This gives a = 1, b = -1, c = -2 x n_pairings

def calc_n_objects(distances):  # Function to calculate the number of objects from a list of separations
    n_pairings = len(distances)
    a = 1
    b = -1
    c = -2 * n_pairings

    discriminant = (b ** 2) - (4 * a * c)  # calculate the discriminant from the quadratic equation

    # Check to see if the discriminant is a perfect square, if not, then we have a problem with the list of distances
    if math.sqrt(discriminant) % 1 == 0:
        print('The discriminant is a perfect square and we can proceed in calculating the number of objects from our '
              'distances list , ')
    else:
        print('The discriminant is not a perfect square and the distances list is missing data')
        return None

    # Calculate the roots to find the number of pairings

    root_1 = (-b + math.sqrt(discriminant)) / 2
    root_2 = (-b - math.sqrt(discriminant)) / 2  # We can ignore root_2 since it will always be negative
    if n_pairings <= 1:
        print('Given the number of separations in your list, we can determine that there are', int(root_1),
              'objects that make up your', n_pairings, 'pairing')
    else:
        print('Given the number of separations in your list, we can determine that there are', int(root_1),
              'objects that make up your', n_pairings, 'pairings')

    return root_1


# ###################################################################################################################### Stage 6 Test the 'number of objects checker' Running this successfully should be a prerequisite for running the binding energy calculation function and should be included in the function itself

calc_n_objects(distances_list)

#######################################################################################################################
# Stage 5 Check that the output is correct
# We know that for when distance = 6.82e-10, u = -1.0e-22 J

# test_distance = [6.82e-10]
# expected_u = -1.0e-22
