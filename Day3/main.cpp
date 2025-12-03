#include <vector>
#include <iostream>
#include <fstream>
#include <string>

struct treeNode {
    int val;
    treeNode* left;
    treeNode* right;

    // Constructor
    treeNode(int value) : val(value), left(nullptr), right(nullptr) {}
};

int MaxValIndex(const std::vector<int>& arr){
    if (arr.empty()) {
        return -1; 
    }

    int maxValIndex = 0;
    for (std::vector<int>::size_type i = 0; i < arr.size(); i++){
        if(arr[i] > arr[maxValIndex]){
            maxValIndex = i;
        }
    }
    return maxValIndex;
}

//recursively constructs the nodes of the tree
treeNode* cartRec(const std::vector<int>& arr){
    if(arr.size() == 0){
        return nullptr;
    }

    int maxValIndex = MaxValIndex(arr);
    treeNode* newNode = new treeNode(arr[maxValIndex]);

    std::vector<int> leftArr(arr.begin(), arr.begin() + maxValIndex);
    std::vector<int> rightArr(arr.begin() + maxValIndex + 1, arr.end());

    newNode->left = cartRec(leftArr);
    newNode->right = cartRec(rightArr);

    return newNode;
}


//constructs the root node for the tree
treeNode* constructRecTree(const std::vector<int>& arr){
    if (arr.empty()) {
        return nullptr;
    }

    int maxValIndex = MaxValIndex(arr);
    treeNode* root = new treeNode(arr[maxValIndex]);

    std::vector<int> leftArr(arr.begin(), arr.begin() + maxValIndex);
    std::vector<int> rightArr(arr.begin() + maxValIndex + 1, arr.end());

    root->left = cartRec(leftArr);
    root->right = cartRec(rightArr);

    return root;
}
//finds the minimum value of a sub array
// int MinValIndex(const std::vector<int>& arr){
//     if (arr.empty()) {
//         return -1; 
//     }

//     int minValIndex = 0;
//     for (std::vector<int>::size_type i = 0; i < arr.size(); i++){
//         if(arr[i] < arr[minValIndex]){
//             minValIndex = i;
//         }
//     }
//     return minValIndex;
// }

int readAndReturn(treeNode* root){
    int left = 0, right = 0;

    if (root->left!=nullptr){
        std::string temp = std::to_string(root->left->val) + std::to_string(root->val);
        left = std::stoi(temp);
    }

    if (root->right!=nullptr){
        std::string temp = std::to_string(root->val)+ std::to_string(root->right->val);
        right = std::stoi(temp);
    }
    return std::max(left,right);
}

std::vector<std::vector<int>> readIn(const std::string& filename){
    std::vector<std::vector<int>> values;
    std::ifstream file(filename);

    if(!file.is_open()){
        std::cerr << "Error opening file\n";
        return values;
    }

    std::string line;
    while(std::getline(file, line)) {
        if(!line.empty()) {
            std::vector<int> digits;
            digits.reserve(line.size());

            for(char c : line){
                if(c >= '0' && c <= '9') {
                    digits.push_back(c-'0');
                }
            }

            values.push_back(std::move(digits));
        }
    }
    return values;
}

// reusing some old code since ive solved this problem before
int main() {
    auto nums = readIn("input.txt");
    int total = 0;

    for(auto& digits: nums){
        treeNode* root = constructRecTree(digits);
        total += readAndReturn(root);
    }
    // std::cout << root->val << std::endl;
    //     if (root->left != nullptr) {
    //     std::cout << root->left->val << std::endl;
    // } else {
    //     std::cout << "Root has no left child." << std::endl;
    // }
    
    // if (root->right != nullptr) {
    //     std::cout << root->right->val << std::endl;
    // } else {
    //     std::cout << "Root has no right child." << std::endl;
    // }

    std::cout << total << std::endl;
    return 0;
}