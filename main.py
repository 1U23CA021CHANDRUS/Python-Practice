class Portfolio:
    def __init__(self, name, role, about):
        self.name = name
        self.role = role
        self.about = about
        self.skills = []
        self.projects = []

    def add_skill(self, skill):
        self.skills.append(skill)

    def add_project(self, title, description):
        self.projects.append({"title": title, "description": description})

    def display_portfolio(self):
        print("=" * 40)
        print(f"       {self.name.upper()} - PORTFOLIO")
        print("=" * 40)
        print(f"Role   : {self.role}")
        print(f"About  : {self.about}\n")
        
        print("Skills :")
        for skill in self.skills:
            print(f"  - {skill}")
        
        print("\nProjects :")
        for proj in self.projects:
            print(f"  * {proj['title']}: {proj['description']}")
        print("=" * 40)

# Portfolio Object create panrathu
if __name__ == "__main__":
    my_portfolio = Portfolio(
        name="Chandru S",
        role="Python Developer",
        about="I am an MCA student interested in software development and programming. I have basic knowledge of Python and enjoy learning new technologies. My goal is to become a skilled Software Developer and build useful software applications."
    )

    my_portfolio.add_skill("Python")
    my_portfolio.add_skill("HTML/CSS")
    my_portfolio.add_skill("Git & GitHub")

    my_portfolio.add_project(
        "Python-Practice", 
        "A repository containing basic to advanced Python coding exercises."
    )
    my_portfolio.add_project(
        "Web Portfolio", 
        "A console/web-based portfolio displaying developer profile."
    )

    my_portfolio.display_portfolio()