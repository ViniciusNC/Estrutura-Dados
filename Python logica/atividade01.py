carros = ["Fusca", "Chevette", "Opala", "Maverick", "Fiorino"]

carros.append("Brasília")

carros.insert(0, "Alfa Romeo")

posicao_opala = carros.index("Opala")

carros.insert(posicao_opala, "Corcel")

carros.remove("Maverick")

print(carros)
