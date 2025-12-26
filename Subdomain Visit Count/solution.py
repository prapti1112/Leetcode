from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        frequencies = {}
        for count_domain in cpdomains:
            count, domain = count_domain.split(" ")
            count, subdomains = int(count), domain.split(".")
            for ind in range(len(subdomains)):
                subdomain = ".".join(subdomains[ind:])
                if subdomain in frequencies:
                    frequencies[subdomain] += count
                else:
                    frequencies[subdomain] = count
        
        return [ f"{value} {key}" for key, value in frequencies.items() ]