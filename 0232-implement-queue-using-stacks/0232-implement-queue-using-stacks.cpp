class MyQueue {
public:
    std::stack<int> stackOne;
    std::stack<int> stackTwo;
    
    MyQueue() {
    }
    
    void push(int x) {
        while(!stackOne.empty()){
            stackTwo.push(stackOne.top());
            stackOne.pop();
        }
        stackOne.push(x);
        while(!stackTwo.empty()){
            stackOne.push(stackTwo.top());
            stackTwo.pop();
        }
    }
    
    int pop() {
        int res = stackOne.top();
        stackOne.pop();
        return res;
    }
    
    int peek() {
        return stackOne.top();
    }
    
    bool empty() {
        if(stackOne.empty()){
            return true;
        }else{
            return false;
        }
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */