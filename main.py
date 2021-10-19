import generic as gen
import graphics
from speciment import Speciment

if __name__ == '__main__':

    generic_result = graphics.log_function()
    graphics.draw_pyplot(generic_result[0], generic_result[1])

    population = []

    for i in range(20):
        population.append(Speciment())

    count = 1
    min_index_speciment = 0

    while True:
        print("Поколение: ", count)
        population = gen.population_reproduction(population)
        gen.population_mutation(population, count)
        population = gen.population_selection(population)
        count += 1
        print('min: ', min(graphics.euclid_distance(population)))
        if min(graphics.euclid_distance(population)) < 0.5:
            euclid_dist = graphics.euclid_distance_test(population)
            min_index_speciment = graphics.euclid_distance(population).index(min(graphics.euclid_distance(population)))
            break

    print('Особь ', population[min_index_speciment].genes)
    print('func', generic_result[1])
    graphics.draw_two_plot(population[min_index_speciment])





