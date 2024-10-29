#include <iostream>
#include <memory>
// using namespace std;
 int main()
 {
    auto p1=std::make_shared<std::string>("这是一个字符串");//std::make_shared<数据类型/类>(参数);
    //返回值：对于类的共享指针 std::make_shared<std::string>
    std::cout << "p1的引用计数："<<p1.use_count()<<"指向内存地址"<<p1.get()<< std::endl;
    auto p2=p1;
    std::cout << "p1的引用计数："<<p1.use_count()<<"指向内存地址"<<p1.get()<< std::endl;
    std::cout << "p2的引用计数："<<p2.use_count()<<"指向内存地址"<<p2.get()<< std::endl;

    p1.reset();//释放引用，不指向
    std::cout << "p1的引用计数："<<p1.use_count()<<"指向内存地址"<<p1.get()<< std::endl;
    std::cout << "p2的引用计数："<<p2.use_count()<<"指向内存地址"<<p2.get()<< std::endl;

    std::cout << "p2数据："<<p2->c_str()<< std::endl;
    
    return 0;
 }