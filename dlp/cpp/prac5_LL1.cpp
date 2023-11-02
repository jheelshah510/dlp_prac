#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

// Define a grammar using a map where non-terminals map to their productions
unordered_map<char, vector<string>> grammar = {
    {'E', {"aX"}},
    {'X', {"+aX", "c"}}
};

unordered_map<char, unordered_set<char>> FIRST;
unordered_map<char, unordered_set<char>> FOLLOW;

void compute_FIRST() {
    bool changed = true;
    
    while (changed) {
        changed = false;
        
        for (const auto& rule : grammar) {
            char nt = rule.first;
            FIRST[nt].clear();
            
            for (const string& prod : rule.second) {
                char firstChar = prod[0];
                
                if (isupper(firstChar)) {
                    if (FIRST.find(firstChar) != FIRST.end()) {
                        unordered_set<char>& firstSet = FIRST[firstChar];
                        size_t originalSize = firstSet.size();
                        
                        FIRST[nt].insert(firstSet.begin(), firstSet.end());
                        
                        if (firstSet.find('') == firstSet.end()) {
                            break;
                        }
                        
                        if (originalSize != firstSet.size()) {
                            changed = true;
                        }
                    }
                } else {
                    FIRST[nt].insert(firstChar);
                    break;
                }
            }
        }
    }
}

void compute_FOLLOW() {
    bool changed = true;
    
    while (changed) {
        changed = false;
        
        for (const auto& rule : grammar) {
            char nt = rule.first;
            
            for (const string& prod : rule.second) {
                for (size_t i = 0; i < prod.size(); ++i) {
                    char current = prod[i];
                    
                    if (isupper(current)) {
                        if (i == prod.size() - 1) {
                            FOLLOW[current].insert(FOLLOW[nt].begin(), FOLLOW[nt].end());
                        } else {
                            for (size_t j = i + 1; j < prod.size(); ++j) {
                                if (isupper(prod[j])) {
                                    FOLLOW[current].insert(FIRST[prod[j]].begin(), FIRST[prod[j]].end());
                                } else {
                                    FOLLOW[current].insert(prod[j]);
                                    break;
                                }
                                
                                if (FIRST[prod[j]].find('') == FIRST[prod[j]].end()) {
                                    break;
                                }
                            }
                        }
                        
                        if (FOLLOW[current].size() != FOLLOW[current].size()) {
                            changed = true;
                        }
                    }
                }
            }
        }
    }
}

bool is_LL1() {
    compute_FIRST();
    compute_FOLLOW();
    
    for (const auto& rule : grammar) {
        char nt = rule.first;
        
        for (const string& prod1 : rule.second) {
            for (const string& prod2 : rule.second) {
                if (&prod1 != &prod2) {
                    if (FIRST[nt].find('') != FIRST[nt].end()) {
                        if (FIRST[nt].size() > 1) {
                            return false;
                        }
                        
                        if (FOLLOW[nt].find('') != FOLLOW[nt].end()) {
                            return false;
                        }
                    }
                    
                    for (char ch : FIRST[nt]) {
                        if (FIRST[prod1[0]].find(ch) != FIRST[prod1[0]].end() &&
                            FIRST[prod2[0]].find(ch) != FIRST[prod2[0]].end()) {
                            return false;
                        }
                    }
                }
            }
        }
    }
    
    return true;
}

int main() {
    if (is_LL1()) {
        cout << "The grammar is LL(1)." << endl;
    } else {
        cout << "The grammar is not LL(1)." << endl;
    }
    
    return 0;
}
