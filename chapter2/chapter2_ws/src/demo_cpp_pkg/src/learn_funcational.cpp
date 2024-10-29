#include <iostream>
#include <functional>//函数包装器头文件
using namespace std;

//自由函数
void save_with_free_fun(const std::string &file_name)
{
    cout <<"free function:"<<file_name<<endl;
}

//成员函数
class FileSave
{
private:
    /* data */
public:
    FileSave(/* args */)=default;
    ~FileSave()=default;
    void save_with_menmber_fun(const std::string &file_name)
    {
        cout <<"chengyuan function:"<<file_name<<endl;
    };
};


int main()
{
    FileSave file_save;
    //Lambda函数
    auto save_with_lambda_fun=[](const std::string &file_name)->void
    {   
        cout <<"Lambda function:"<<file_name<<endl;
    };

    // save_with_free_fun("file.txt");
    // file_save.save_with_menmber_fun("file.txt");
    // save_with_lambda_fun("file.txt");
    //将三种函数放入包装器
    std::function<void(const std::string &)> save1=save_with_free_fun;
    std::function<void(const std::string &)> save2=save_with_lambda_fun;
    std::function<void(const std::string &)> save3=std::bind(&FileSave::save_with_menmber_fun,
    &file_save,std::placeholders::_1);//参数1：成员函数方法名；参数2：变量；参数3：对于参数个数

    //统一调用方法
    save1("file.txt");
    save2("file.txt");
    save3("file.txt");
    return 0;
}
