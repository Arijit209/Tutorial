class coffeeMachine {
    start() {
        this.#addWater();
        this.#addCoffeePowder();
        this.#boilWater();
        this.#pourCoffee();
        console.log("Starting the coffee machine...");
    }
    #addWater() {
        console.log("Adding water...");
    }
    #addCoffeePowder() {
        console.log("Adding coffee powder...");
    }
    #boilWater() {
        console.log("Boiling water...");
    }
    #pourCoffee() {
        console.log("Pouring coffee...");
    }
}

const machine = new coffeeMachine();
machine.start();


