#include <iostream>

class singleton {
private:
    static singleton *instance;
    singleton();
public:
    static singleton * getInstance(void);
};

singleton* singleton::instance =  (singleton*)0;

singleton* singleton::getInstance() {
    if (instance != (singleton*) 0){
        return(instance);
    } else {
        instance = new singleton;
        return (instance);
    }
}

singleton::singleton() {}

int main() {
    std::cout << "instatiating a couple of singletons:" << std::endl;
    singleton *instance_a = singleton::getInstance();
    printf("%p\n", instance_a); //<< std::endl;
    singleton *instance_b = singleton::getInstance();
    printf("%p\n", instance_b); //<< std::endl;
    singleton *instance_c = singleton::getInstance();
    printf("%p\n", instance_c); //<< std::endl;
    return 0;
}