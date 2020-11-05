#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

vector<int> goal = {1, 2, 3, 8, 0, 4, 7, 6, 5};

float h1(vector<int> &goal, vector<int> &arr)
{
    float sm = 0;
    for (int count = 0; count < 9; count++)
    {
        sm += (goal[count] != arr[count]);
    }
    return sm;
}

int getId(vector<int> &arr)
{
    int sm = 0;
    for (int i = 8; i > -1; i--)
    {
        sm += ceil((arr[i]) * pow(10, 8 - i));
    }
    return sm;
}

class node
{
public:
    vector<int> arr;
    int id;
    node *next;
    node *parent;
    node *child;
    float hval;
    float g;
    float total;
    node(vector<int> &arr);
    void display();
    void details();
};
void node::details()
{
    cout << "{id:" << this->id << "}"
         << "{g:" << this->g << "}"
         << "{h:" << this->hval << "}"
         << "{total:" << this->total << "}\n";
}

node::node(vector<int> &arr)
{
    this->id = getId(arr);
    this->arr = arr;
    this->g = 0;
    this->hval = h1(goal, this->arr);
    this->total = this->hval + this->g;
    this->next = NULL;
    this->parent = NULL;
    this->child = NULL;
}
void node::display()
{
    for (int i = 0; i < 9; i++)
    {
        cout << this->arr[i] << " ";
        if (i % 3 == 2)
        {
            cout << endl;
        }
    }
}

class list
{
public:
    node *head;
    list() : head(NULL) {}
    void insert(node *tmp);
    void display();
    node *getBest();
};
node *list::getBest()
{
    node *best;
    best = this->head;
    this->head = best->next;
    best->next = NULL;
    return best;
}
void list::display()
{
    node *pnt = this->head;
    if (pnt == NULL)
    {
        cout << "LIST IS EMPTY!!!" << endl;
        return;
    }
    while (pnt != NULL)
    {
        cout << pnt->id << ":" << pnt->total << " ";
        pnt = pnt->next;
    }
    cout << endl;
}
void list::insert(node *tmp)
{
    if (this->head == NULL)
    {
        this->head = tmp;
    }
    else
    {
        if (tmp->total < this->head->total)
        {
            tmp->next = this->head;
            this->head = tmp;
        }
        else
        {
            node *pnt = this->head;
            node *tnt = NULL;
            while (pnt != NULL)
            {
                if ((tmp->total < pnt->total))
                {
                    break;
                }
                tnt = pnt;
                pnt = pnt->next;
            }
            tmp->next = tnt->next;
            tnt->next = tmp;
        }
    }
}

list OPEN;
list CLOSED;

void insertSuccessor(node *n)
{
    node *open = OPEN.head;
    node *tail = NULL;
    // n->display();
    while (open != NULL)
    {
        if (open->id == n->id)
        {
            if (open->total > n->total)
            {
                if (tail != NULL)
                {
                    tail->next = open->next;
                }
                else
                {
                    OPEN.head = NULL;
                }
                OPEN.insert(n);
                return;
            }
        }
        tail = open;
        open = open->next;
    }
    open = CLOSED.head;
    tail = NULL;
    while (open != NULL)
    {
        if (open->id == n->id)
        {
            if (open->total > n->total)
            {
                if (tail != NULL)
                {
                    tail->next = open->next;
                }
                else
                {
                    CLOSED.head = NULL;
                }
                CLOSED.insert(n);
                return;
            }
        }
        tail = open;
        open = open->next;
    }
    OPEN.insert(n);
}

void getSuccessor(node p, vector<node> &successor)
{
    int zero;
    vector<int> arr;
    for (int i = 0; i < 9; i++)
    {
        arr.push_back(p->arr[i]);
        if (p->arr[i] == 0)
        {
            zero = i;
        }
    }
    vector<int> positions;
    int zr = zero / 3;
    int zc = zero % 3;
    if (zr == 0)
    {
        if (zc == 0)
        {
            positions = {1, 3};
        }
        else if (zc == 1)
        {
            positions = {0, 2, 4};
        }
        else if (zc == 2)
        {
            positions = {1, 5};
        }
    }
    if (zr == 1)
    {
        if (zc == 0)
        {
            positions = {0, 4, 6};
        }
        else if (zc == 1)
        {
            positions = {1, 4, 5, 7};
        }
        else if (zc == 2)
        {
            positions = {2, 4, 8};
        }
    }
    if (zr == 2)
    {
        if (zc == 0)
        {
            positions = {4, 7};
        }
        else if (zc == 1)
        {
            positions = {4, 6, 8};
        }
        else if (zc == 2)
        {
            positions = {5, 7};
        }
    }
    for (int i = 0; i < positions.size(); i++)
    {
        vector<int> temp;
        for (int i = 0; i < 9; i++)
        {
            temp.push_back(p->arr[i]);
            if (p->arr[i] == 0)
            {
                zero = i;
            }
        }
        int val = temp[positions[i]];
        temp[positions[i]] = 0;
        temp[zero] = val;
        successor.push_back(new node(temp));
        successor[i]->parent = p;
        successor[i]->g = 1 + p->g;
        successor[i]->total = successor[i]->g + successor[i]->hval;
    }
}

void victoryStep(node *best)
{
    if (best == NULL)
    {
        cout << "\nINITIAL NODE!!\n-----" << endl;
    }
    else
    {
        victoryStep(best->parent);
        best->display();
        cout << "-----" << endl;
    }
}
int main()
{
    vector<int> initialArray = {
        0, 3, 5,
        2, 1, 4,
        8, 7, 6};
    node INIT = node(initialArray);
    OPEN.insert(&INIT);
    node *BEST;
    BEST = OPEN.getBest();
    CLOSED.insert(BEST);
    int step = 0;
    while (BEST->hval != 0)
    {
        cout << "STEP " << ++step << endl;
        vector<node *> SUCCESSORS;
        getSuccessor(BEST, SUCCESSORS);
        for (int i = 0; i < SUCCESSORS.size(); i++)
        {
            insertSuccessor(SUCCESSORS[i]);
        }
        BEST = OPEN.getBest();
        CLOSED.insert(BEST);
        // cout<<"OPEN  : ";
        // OPEN.display();
        // cout<<"CLOSED: ";
        // CLOSED.display();
        // cout<<"----------------------------------------"<<endl;
        if (step > 500000)
        {
            cout << "Solution not found in 30 step." << endl;
            return 0;
        }
    }
    victoryStep(BEST);
    cout << "Cost of getting to goal: " << BEST->g << endl;
    return 0;
}