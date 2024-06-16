

public class MainClass {
    public static void main(String[] args) {
        Animal genericAnimal = new Animal("GenericAnimal");
        genericAnimal.makeSound();

        Dog dog = new Dog("Buddy");
        dog.makeSound();
        dog.fetch();
    }
}
