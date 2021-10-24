#include <iostream>
#include <vector>

template<typename T>
class TreeNode {
public:
    TreeNode(const T& n, TreeNode* left = NULL, TreeNode* right = NULL)
            : mValue(n),
              mLeft(left),
              mRight(right) {}

    T getValue() const {
        return mValue;
    }

    TreeNode* left() const {
        return mLeft;
    }

    TreeNode* right() const {
        return mRight;
    }

    void preorderTraverse() const {
        std::cout << " " << getValue();
        if(mLeft)  { mLeft->preorderTraverse();  }
        if(mRight) { mRight->preorderTraverse(); }
    }

    void inorderTraverse() const {
        if(mLeft)  { mLeft->inorderTraverse();  }
        std::cout << " " << getValue();
        if(mRight) { mRight->inorderTraverse(); }
    }

    void postorderTraverse() const {
        if(mLeft)  { mLeft->postorderTraverse();  }
        if(mRight) { mRight->postorderTraverse(); }
        std::cout << " " << getValue();
    }

    void levelOrderTraverse()  {

        T RValue = 0;
        T LValue = 0;
        if(mLeft)  { LValue = mLeft->getValue(); }
        if(mRight) { RValue = mRight->getValue(); }
        std::vector<T> LevelRow(RValue, LValue);
        Levels.push_back(LevelRow);

        if(mLeft)  { mLeft->levelOrderTraverse();  }
        if(mRight) { mRight->levelOrderTraverse(); }

    }

    void PrintLevelOrderTraverse() {
        for (size_t i = 0; i < Levels.size(); i++) {
            for (size_t j = 0; j < Levels[i].size(); j++) {
                std::cout << Levels[i][j];
            }
            std::cout << std::endl;
        }
    }
protected:
    T mValue;
    TreeNode* mLeft;
    TreeNode* mRight;
    int64_t TreeLevel = 0;
    std::vector<std::vector<T>> Levels;

private:
    TreeNode();
};

int main() {
    TreeNode<int> root(1,
            new TreeNode<int>(2,
                    new TreeNode<int>(4,
                            new TreeNode<int>(7)),
                    new TreeNode<int>(5)),
            new TreeNode<int>(3,
                    new TreeNode<int>(6,
                            new TreeNode<int>(8),
                            new TreeNode<int>(9))));
/*
    std::cout << "preorder:   ";
    root.preorderTraverse();
    std::cout << std::endl;

    std::cout << "inorder:    ";
    root.inorderTraverse();
    std::cout << std::endl;

    std::cout << "postorder:  ";
    root.postorderTraverse();
    std::cout << std::endl;
*/
    //std::cout << "level-order:";
    root.levelOrderTraverse();
    //root.PrintLevelOrderTraverse();
    //std::cout << std::endl;

    return 0;
}