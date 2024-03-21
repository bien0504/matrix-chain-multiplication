import dp
import greedy
# import genetic_algorithm
import get_data
import brute_force

if __name__=="__main__":
    get_data.init_random_data(20, 5, 10,'input.txt')

    data=get_data.get_data("input.txt")
    greedy.solve(data)
    dp.solve(data)
    brute_force.solve(data)
    print("Hello world")
