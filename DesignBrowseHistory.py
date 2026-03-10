class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.curr_page = 0

    def visit(self, url: str) -> None:
        while self.curr_page != len(self.pages) - 1:
            self.pages.pop()

        self.pages.append(url)
        self.curr_page += 1

    def back(self, steps: int) -> str:
        self.curr_page = max(0, self.curr_page - steps)
        return self.pages[self.curr_page]

    def forward(self, steps: int) -> str:
        self.curr_page = min(self.curr_page + steps, len(self.pages) - 1)
        return self.pages[self.curr_page]      
