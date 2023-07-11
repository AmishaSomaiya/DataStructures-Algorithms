"""
https://leetcode.com/problems/combination-sum/

leetcode 721
medium
DFS + hashtable

input : a list of accounts where each element accounts[i] is a list of strings, 
where the first element accounts[i][0] is a name, and the rest of the elements are emails 
representing emails of the account.
output: List[List[str]] merged accounts

brute force :
iterate for every email in each account and check if there is another account having the same 
email. 

improved solution :
-build an email map that helps look-up for its account in constant time (the first email are 
used for key in this problem). Each email in the same account are paired with the first email.
-i.e. connect emails in an account in a star manner with the first email as the internal node 
of the star and all other emails as the leaves. 
-After constructing the map, run DFS for every email not visited yet. 
-In each iteration of DFS, mark this email as visited so that do not visit it again. I
-in addition, reach back to the internal node of that star with the email map we built earlier.
-By knowing the internal node, run DFS again for every unvisited email for that internal node.

Time Complexity: O(nmlognm)
where n = the number of accounts and m = the maximum number of emails in one account. 
In worst case, all emails belong to one person. Therefore, sorting n*m emails will need 
O(nmlognm) time, while building emails map and running DFS both will cost O(nm) time as no 
email will be traversed more than once. These procedures result in O(nmlognm) time complexity.
Space Complexity: O(nm) for emails map.

"""
from collections import defaultdict
from typing import List

def accountsMerge(accounts):
    def DFS(email):
        visitedemails.add(email)
        mergedemails.append(email)

        for newemail in emailmap[email]:
            if newemail not in visitedemails:
                DFS(newemail)

    # Construct emails map for constant look-up speed
    emailmap = defaultdict(list)
    for account in accounts:
        firstemail = account[1]
        for i in range(2, len(account)):
            email = account[i]
            emailmap[firstemail].append(email)
            emailmap[email].append(firstemail)

    mergedaccounts, visitedemails = [], set()
    for account in accounts:
        name, firstemail = account[0], account[1]
        if firstemail not in visitedemails:
            mergedemails = []
            DFS(firstemail)
            mergedaccounts.append([name] + sorted(mergedemails))

    return mergedaccounts


print(accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))

print(accountsMerge([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]))