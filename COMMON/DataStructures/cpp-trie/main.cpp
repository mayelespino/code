#include <iostream>
#include <map>
using namespace std;


struct TrieNode {
    bool flag;
    map<char, TrieNode*> next;
};

class Trie {
private:
    TrieNode* root;

public:
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode();
    }

    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode* p = root;
        for (int i = 0; i < word.length(); ++i) {
            if ((p->next).count(word[i]) <= 0) {
                // insert a new node if the path does not exist
                (p->next).insert(make_pair(word[i], new TrieNode()));
            }
            p = (p->next)[word[i]];
        }
        p->flag = true;
    }

    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode* p = root;
        for (int i = 0; i < word.length(); ++i) {
            if ((p->next).count(word[i]) <= 0) {
                return false;
            }
            p = (p->next)[word[i]];
        }
        return p->flag;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode* p = root;
        for (int i = 0; i < prefix.length(); ++i) {
            if ((p->next).count(prefix[i]) <= 0) {
                return false;
            }
            p = (p->next)[prefix[i]];
        }
        return true;
    }

    bool printCurrentNode(map<char, TrieNode*> currentNode) {
 // cout << (currentNode['a'])['p'];
        for (auto x : currentNode) {
            cout << x.first << " ";
            printCurrentNode(x.second->next);
        }
    }

    void printTrie(void) {
        TrieNode* p = root;
        printCurrentNode(p->next);
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * bool param_2 = obj.search(word);
 * bool param_3 = obj.startsWith(prefix);
 */

int main(int argc, char **argv){
    Trie aTrie = Trie();
    aTrie.insert("a");
    aTrie.insert("append");
    aTrie.insert("appendix");
    aTrie.startsWith("ap") ?  cout << "starts with ap" << endl : cout << "does not start with ap" << endl;
    aTrie.printTrie();
    return 0;
}