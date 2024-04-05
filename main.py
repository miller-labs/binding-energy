# Date created: 04/04/2024
# Date modified:
# Created by: Joel Miller
# This is a project to calculate the binding energy of "n" number of objects for a given geometry.
# Initially we would just like to know the binding energy of 3 objects for a given geometry.

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

distances_list = [r1_2, r1_3, r2_3]  # List of all distances between each of the objects

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


def total_binding_energy_calc(distances):
    binding_energies_list = []  # Initialize empty list to store calculate binding energies of individual pairs

    for r in distances:
        binding_energy = binding_energy_calc(r)
        binding_energies_list.append(binding_energy)

    total_binding_energy = sum(binding_energies_list)

    n = len(distances)
    n_pairings = (n * (n - 1)) / 2
    if n <= 1:
        print('There is', n, 'separation in this list')
        print('The total binding energy of the', n, 'separation is', total_binding_energy, 'J')
    else:
        print('There are', n, 'separations in this list')
        print('The total binding energy of the', n, 'separations is', total_binding_energy, 'J')
    # print('Number of Pairings is ', int(n_pairings))

    print(n_pairings)
    return total_binding_energy


#######################################################################################################################
# Run the programme to calculate the total binding energy

total_binding_energy_calc(distances_list)

# If we are given a list with an incorrect number of separations, then our calculation for the total binding energy
# will be incorrect. For instance, 10 objects provides 27 pairings. If we have a list containing 28 pairings,
# then we end up with a non-integer number of objects, which is impossible. We can use this information to include a
# check within our code, that tells us if we have a reasonable number of elements in our list. Of course, it's possible
# that we randomly end up with a list containing a reasonable number of elements; however, this check minimises the
# chance of the code outputting the incorrect result

# To do this I can take the equation: n_pairings = (n * (n - 1)) / 2, and rearrange for n.
# This gives gives a quadratic equation (n^2 − n − 2 x n_pairings = 0), which can be solved using the quadratic formula.

#######################################################################################################################
# Stage 5 Check that the output is correct
# We know that for when distance = 6.82e-10, u = -1.0e-22 J

# test_distance = [6.82e-10]
# expected_u = -1.0e-22

# test_binding_energies_list = []  # Initialize empty list to store calculate binding energies of individual pairs

# for i in test_distance:
#    binding_energy = binding_energy_calculation(i)
#    test_binding_energies_list.append(binding_energy)

# total_binding_energy = sum(test_binding_energies_list)

# print('Total binding energy of the', n, 'objects is', total_binding_energy, 'J')
