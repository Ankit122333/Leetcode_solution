class Solution {
public:
    vector <string> cellsInRange(string s) {
        int r1=s[1]-'0',r2=s[4]-'0';
        int c1=s[0]-'A',c2=s[3]-'A';
        vector <string> ans;
        for(int i=c1;i<=c2;i++)
        {
            for(int j=r1;j<=r2;j++)
            {
                string x="";
                x+=(char)(i+'A');
                x+=to_string(j);
                ans.push_back(x);
            }
        }
        return ans;
        
    }
};