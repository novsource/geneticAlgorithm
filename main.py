import generic
import graphics
import speciment

if __name__ == '__main__':
    generic_result = generic.generic_log_function()
    graphics.draw_pyplot(generic_result[0], generic_result[1])
    spec = speciment.Speciment()
    spec2 = speciment.Speciment()
    generic.reproduction_speciment(spec, spec2)
    spec.mutation()


