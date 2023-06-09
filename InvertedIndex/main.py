from controllers.table_controller import TableController


if __name__ == "__main__":
    controller = TableController(("Animal", "Classe", "Estado de conservação", "Peso médio (Kg)"))
    controller.add_data_dev(["RAPOSA", "MAMMALIA", "LC", "8,5"])
    controller.add_data_dev(["COALA", "MAMMALIA", "VU", "10"])
    controller.add_data_dev(["PANDA", "MAMMALIA", "VU", "117,5"])
    controller.add_data_dev(["DONINHA", "MAMMALIA", "LC", "0,143"])
    controller.add_data_dev(["CAMALEAO", "REPTILIA", "LC", "2,2"])
    controller.add_data_dev(["IGUANA-DO-CARIBE", "REPTILIA", "CR", "4,23"])
    controller.add_data_dev(["CORVO", "AVES", "LC", "1,2"])
    controller.add_data_dev(["DODO", "AVES", "EX", "14,05"])
    controller.add_data_dev(["ARARINHA-AZUL", "AVES", "EW", "1,47"])
    controller.add_data_dev(["LOBO-GUARA", "MAMMALIA", "NT", "25"])
    controller.add_data_dev(["COBRA-DO-MILHO", "REPTILIA", "LC", "3,21"])
    controller.add_data_dev(["FURAO", "MAMMALIA", "DM", "6,5"])
    controller.open_view()