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

    for i in range(100):
        print("Поколение: ", count)
        population = gen.population_reproduction(population)
        gen.population_mutation(population)
        population = gen.population_selection(population)
        count += 1

    graphics.draw_pyplot(population[0].signs, population[0].genes)





