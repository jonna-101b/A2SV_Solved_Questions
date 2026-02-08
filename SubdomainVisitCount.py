from typing import List

class Solution:
    def __init__(self):
        self.domains = dict()

    def storeDomains(self, visits: List[str], domains: List[str]) -> None:
        visits = int("".join(visits))
        domain_so_far = ""
        for i in range(len(domains) - 1, -1, -1):
            domain_so_far = domains[i] if domain_so_far == "" else domains[i] + "." + domain_so_far
            
            if domain_so_far in self.domains:
                self.domains[domain_so_far] += visits
                continue

            self.domains[domain_so_far] = visits

    def createSubdomainList(self) -> List[str]:
        subdomain_visits = []

        for domain in self.domains:
            cpdomain = f"{self.domains[domain]} {domain}"
            subdomain_visits.append(cpdomain)

        return subdomain_visits

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        for cpdomain in cpdomains:
            visits = []
            domain = []
            domains = []
            
            for char in cpdomain:
                if char == " ":
                    continue

                elif char.isdigit():
                    visits.append(char)

                elif char == ".":
                    domain_joined = "".join(domain)
                    domains.append(domain_joined)
                    domain = []

                else:
                    domain.append(char)

            domain_joined = "".join(domain)
            domains.append(domain_joined)
            self.storeDomains(visits, domains)

        return self.createSubdomainList()