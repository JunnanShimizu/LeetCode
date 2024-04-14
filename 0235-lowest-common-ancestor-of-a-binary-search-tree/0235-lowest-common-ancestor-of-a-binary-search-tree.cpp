/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* curNode = root;
        
        while(curNode != NULL){
            if(p->val < curNode->val && q->val < curNode->val){
                curNode = curNode->left;
            }else if(p->val > curNode->val && q->val > curNode->val){
                curNode = curNode->right;
            }else{
                return curNode;
            }
        }
        
        return NULL;
    }
};