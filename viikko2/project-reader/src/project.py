class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        def format_list(items):
            return "\n".join(f"- {item}" for item in items) if items else "-"

        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\nAuthors:\n{format_list(self.authors)}"
            f"\n"
            f"\nDependencies:\n{format_list(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies:\n{format_list(self.dev_dependencies)}"
        )