from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon_list = []

    def add_pokemon(self, pokemon_obj):
        if pokemon_obj in self.pokemon_list:
            return "This pokemon is already caught"
        else:
            self.pokemon_list.append(pokemon_obj)
            # return f"Caught {pokemon_obj.name} with health {pokemon_obj.health}"
            return f"Caught {pokemon_obj.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        for x in self.pokemon_list:
            if x.name == pokemon_name:
                self.pokemon_list.remove(x)
                return f"You have released {pokemon_name}"
            else:
                return f"Pokemon is not caught"

    def trainer_data(self):
        # result = ""
        # result += f"Pokemon Trainer {self.name}\n"
        # result += f"Pokemon count {len(self.pokemon_list)}\n"
        # for x in self.pokemon_list:
        #     result += f"- {x.pokemon_details()}\n"
        # return result

        info_pokemons = ''
        for x in self.pokemon_list:
            info_pokemons += f"- {x.pokemon_details()}" + "\n"
        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon_list)}\n" + info_pokemons


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
