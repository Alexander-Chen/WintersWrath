#include <iostream>
#include <malloc.h>
using namespace std;

class Obj
{
public :
    Obj(void){ cout << "  Initialization" << endl; }
    ~Obj(void){ cout << "  Destroy" << endl; }
    void Initialize(void){ cout << "  Initialization" << endl; }
    void Destroy(void){ cout << "  Destroy" << endl; }
};

void UseMallocFree(void)
{
    Obj  *a = (Obj *)malloc(sizeof(Obj));   // ���붯̬�ڴ�
    a->Initialize();                        // ��ʼ��
    //��
    a->Destroy();   // �������
    free(a);        // �ͷ��ڴ�
}

void UseNewDelete(void)
{
    Obj  *a = new Obj;  // ���붯̬�ڴ沢�ҳ�ʼ��
    //��
    delete a;           // ��������ͷ��ڴ�
}

int main(void)
{
	cout << "Use Malloc-Free Method:" << endl;
	UseMallocFree();
	cout << endl;
	cout << "Use New-Delete Method:" << endl;
	UseNewDelete();

	getchar();
	return 0;
}