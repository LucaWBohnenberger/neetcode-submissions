class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> dicionario = {{'[',']'}, {'{','}'}, {'(',')'}};
        unordered_set<char> fechamentos = {']', '}', ')'};
        vector<char> esperados;

        if (s.size() == 1 || fechamentos.count(s[0])){
            return false;
        }
        
        for (char term : s){
            if (dicionario.count(term)){
                esperados.push_back(dicionario[term]);
            }else{
                if (esperados.size() == 0 || esperados.back() != term){
                    return false;
                }else{
                    esperados.pop_back();
                }
            }
        }

        if (esperados.size() == 0){
            return true;
        }
        return false;
    }
};
