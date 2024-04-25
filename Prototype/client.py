from deathclaw_variants import Regular, Legendary, Young, Mother, Irradiated

class DeathclawCache:
    cache = {}

    @staticmethod
    def get_deathclaw(variant):
        deathclaw = DeathclawCache.cache.get(variant, None)
        return deathclaw.clone()

    @staticmethod
    def load():
        regular = Regular()
        DeathclawCache.cache[regular.variant] = regular

        legendary = Legendary()
        DeathclawCache.cache[legendary.variant] = legendary

        young = Young()
        DeathclawCache.cache[young.variant] = young

        mother = Mother()
        DeathclawCache.cache[mother.variant] = mother

        irradiated = Irradiated()
        DeathclawCache.cache[irradiated.variant] = irradiated


if __name__ == '__main__':
    DeathclawCache.load()

    regular1 = DeathclawCache.get_deathclaw("Deathclaw")
    print(f"{regular1.variant}, HP - {regular1.hp}, Melee Damage - {regular1.melee}")

    regular2 = DeathclawCache.get_deathclaw("Deathclaw")
    print(f"{regular2.variant}, HP - {regular2.hp}, Melee Damage - {regular2.melee}")

    # Explicação:
    # Aqui, podemos facilmente criar um Deathclaw quantas vezes quisermos, apenas instanciando protótipos.

    young = DeathclawCache.get_deathclaw("Young Deathclaw")
    print(f"{young.variant}, HP - {young.hp}, Melee Damage - {young.melee}")

    mother = DeathclawCache.get_deathclaw("Deathclaw Mother")
    print(f"{mother.variant}, HP - {mother.hp}, Melee Damage - {mother.melee}")

    irradiated = DeathclawCache.get_deathclaw("Irradiated Deathclaw")
    print(f"{irradiated.variant}, HP - {irradiated.hp}, Melee Damage - {irradiated.melee}")

    legendary = DeathclawCache.get_deathclaw("Legendary Deathclaw")
    print(f"{legendary.variant}, HP - {legendary.hp}, Melee Damage - {legendary.melee}")

