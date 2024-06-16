

public class Dog extends Animal {

    public Dog(String name) {
        super(name);
       
    }
    
     @Override
    public void makeSound() {
        System.out.println("Bark");
    }

    public void fetch() {
        System.out.println(getName() + " is fetching the ball");
    }
}
