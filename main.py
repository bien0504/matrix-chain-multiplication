import dp
import greedy
# import genetic_algorithm
import get_data
import brute_force
max_number_of_nodes=10
if __name__=="__main__":
    get_data.init_random_data(9, 5, 10,'input.txt')

    data=get_data.get_data("input.txt")
    greedy.solve(data)
    dp.solve(data)
    if(len(data)<max_number_of_nodes):
        brute_force.solve(data)
    print("Hello world")
