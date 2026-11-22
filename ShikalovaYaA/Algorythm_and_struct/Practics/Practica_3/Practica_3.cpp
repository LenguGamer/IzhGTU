#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Node {
    string name;
    Node* nextNode;
    Node* prevNode;

    Node(const string& val) {
        name = val;
        nextNode = nullptr;
        prevNode = nullptr;
    }
};

struct DoubleLinkList {
    Node* head;
    Node* tail;
    int count;

    DoubleLinkList() {
        head = nullptr;
        tail = nullptr;
        count = 0;
    }

    virtual void push_front(const string& val) {
        Node* newNode = new Node(val);
        if (head == nullptr) {
            head = tail = newNode;
        }
        else {
            newNode->nextNode = head;
            head->prevNode = newNode;
            head = newNode;
        }
        count++;
    }

    virtual void push_back(const string& val) {
        Node* newNode = new Node(val);
        if (tail == nullptr) {
            tail = head = newNode;
        }
        else {
            tail->nextNode = newNode;
            newNode->prevNode = tail;
            tail = newNode;
        }
        count++;
    }

    virtual void pop_front() {
        if (head == nullptr) return;
        if (head == tail) {
            delete head;
            head = nullptr;
            tail = nullptr;
        }
        else {
            head = head->nextNode;
            delete head->prevNode;
            head->prevNode = nullptr;
        }
        count--;
    }

    virtual void pop_back() {
        if (head == nullptr) return;
        if (head == tail) {
            delete head;
            head = nullptr;
            tail = nullptr;
        }
        else {
            tail = tail->prevNode;
            delete tail->nextNode;
            tail->nextNode = nullptr;
        }
        count--;
    }

    virtual void pop_node(Node* node) {
        if (head == nullptr || node == nullptr) return;
        if (node == head) pop_front();
        else if (node == tail) pop_back();
        else {
            node->prevNode->nextNode = node->nextNode;
            node->nextNode->prevNode = node->prevNode;
            delete node;
            count--;
        }
    }

    virtual void insert_after(Node* node, const string& val) {
        if (node == nullptr) return;
        if (node == tail) push_back(val);
        else {
            Node* newNode = new Node(val);
            node->nextNode->prevNode = newNode;
            newNode->nextNode = node->nextNode;
            node->nextNode = newNode;
            newNode->prevNode = node;
            count++;
        }
    }

    virtual void print() {
        if (head == nullptr) return;
        Node* i = head;
        while (i != tail) {
            cout << i->name << " ";
            i = i->nextNode;
        }
        cout << tail->name;
    }

    virtual ~DoubleLinkList() {
        while (head != nullptr) {
            pop_front();
        }
    }
};

struct CircleDoubleLinkList : public DoubleLinkList {
    void push_back(const string& val) override {
        Node* newNode = new Node(val);
        if (head == nullptr) {
            head = tail = newNode;
            head->nextNode = head;
            head->prevNode = head;
        }
        else {
            tail->nextNode = newNode;
            newNode->prevNode = tail;
            head->prevNode = newNode;
            newNode->nextNode = head;
            tail = newNode;
        }
        count++;
    }

    void push_front(const string& val) override {
        Node* newNode = new Node(val);
        if (head == nullptr) {
            head = tail = newNode;
            newNode->nextNode = newNode;
            newNode->prevNode = newNode;
        }
        else {
            tail->nextNode = newNode;
            newNode->prevNode = tail;
            head->prevNode = newNode;
            newNode->nextNode = head;
            head = newNode;
        }
        count++;
    }

    void pop_back() override {
        if (head == nullptr) return;
        if (head == tail) {
            delete head;
            head = nullptr;
            tail = nullptr;
        }
        else {
            head->prevNode = tail->prevNode;
            tail->prevNode->nextNode = head;
            delete tail;
            tail = head->prevNode;
        }
        count--;
    }
    //Время 0:53. Мне очень нравятся двусвязные списки
    void pop_front() override {
        if (head == nullptr) return;
        if (head == tail) {
            delete head;
            head = nullptr;
            tail = nullptr;
        }
        else {
            tail->nextNode = head->nextNode;
            head->nextNode->prevNode = tail;
            delete head;
            head = tail->nextNode;
        }
        count--;
    }

    ~CircleDoubleLinkList() override {
        if (head != nullptr) {
            tail->nextNode = nullptr;
            head->prevNode = nullptr;
        }
    }
};

string SpisokJosephaShindlera(int n, int m, const vector<string>& names) {
    CircleDoubleLinkList circle;
    for (int i = 0; i < n; i++) {
        circle.push_back(names[i]);
    }

    Node* i = circle.head;

    while (circle.count > 1) {
        for (int step = 1; step < m; step++) {
            i = i->nextNode;
        }
        Node* stop = i->nextNode;
        circle.pop_node(i);
        i = stop;
    }
    return circle.head->name;
}

string SpisokJosephaShindleraMath(int n, int m, const vector<string>& names) {
    int winnerIndex = 0;
    for (int i = 2; i <= n; ++i) {
        winnerIndex = (winnerIndex + m) % i;
    }
    return names[winnerIndex];
}

//Время 1:18. 3я практика выполнена. Главное не забыть запушить её.
int main() {
    return 0;
}