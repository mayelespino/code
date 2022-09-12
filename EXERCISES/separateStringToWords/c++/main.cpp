#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool isWordInDict(const string aWord, const string dict[]){
    for(unsigned int idx = 0; idx < sizeof(dict); idx += 1){
        if(aWord == dict[idx])
            return true;
    }
    return false;
}
bool canSeparateInWords(const string sourceString, const string words[]){
    string aWord = "";
    bool canBeSeparated = false;
    for (char const &c: sourceString) {
        aWord += c;
        if(isWordInDict(aWord, words)) {
            canBeSeparated = true;
            aWord.clear();
        } else {
            canBeSeparated = false;
        }
    }
    return canBeSeparated;
}

vector<string> separateInWords(const string sourceString, const string words[]) {
    string aWord = "";
    bool canBeSeparated = false;
    std::vector<std::string> separateWords;
    for (char const &c: sourceString) {
        aWord += c;
        if(isWordInDict(aWord, words)) {
            canBeSeparated = true;
            separateWords.push_back(aWord);
            aWord.clear();
        } else {
            canBeSeparated = false;
        }


    }

    if(canBeSeparated)
        return separateWords;
    else
        return {};
}

int main() {
    string words[4] = {"apple","cart", "my", "the"};

    string sourceString = "applemycart";
    for(auto&& w: words)
        cout << w << " ";
    cout << "<-->" << sourceString << endl;

    if(canSeparateInWords(sourceString, words))
        cout << "True" << endl;
    else
        cout << "False" << endl;

    vector<string> separateWords = separateInWords(sourceString, words);
    for(auto&& w: separateWords)
        cout << w << endl;

    cout << "==========" << endl;


    string sourceString2 = "appleXcart";
    for(auto&& w: words)
        cout << w << " ";
    cout << "<-->" << sourceString2 << endl;

    if(canSeparateInWords(sourceString2, words))
        cout << "True" << endl;
    else
        cout << "False" << endl;

    vector<string> separateWords2 = separateInWords(sourceString2, words);
    for(auto&& w: separateWords2)
        cout << w << endl;

    cout << "==========" << endl;


    string sourceString3 = "xxxapplecartthe";
    for(auto&& w: words)
        cout << w << " ";
    cout << "<-->" << sourceString3 << endl;

    if(canSeparateInWords(sourceString3, words))
        cout << "True" << endl;
    else
        cout << "False" << endl;

    vector<string> separateWords3 = separateInWords(sourceString3, words);
    for(auto&& w: separateWords3)
        cout << w << endl;

    cout << "==========" << endl;

    return 0;
}
