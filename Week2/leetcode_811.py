from collections import deque
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = {}
        for domain in cpdomains:
            rep, d_str = domain.split(' ')
            rep = int(rep)
            d_list = d_str.split('.')

            for d in range(len(d_list) - 1, -1, -1):
                domain = '.'.join(d_list[d:len(d_list)])
                if domain not in domains:
                    domains[domain] = 0
                domains[domain] += rep

        return [f'{value} {key}' for key, value in domains.items()]
            