import os
import json
from rich import print
from .utils.skill_trees import ParseSkills


class AddSkills:
    def __init__(self) -> None:
        self.languages = {
            "python": ["py", "python"],
            "pandas": ["py", "python"],
            "numpy": ["py", "python"],
            "matplotlib": ["py", "python"],
            "sklearn": ["py", "python"],
            "ml": ["py", "python"],
            "opencv": ["py", "python"],
            "django": ["py", "python"],
            "pygame": ["py", "python"],
            "tkinter": ["py", "python"],
            "linux": ["bash", "shell"],
            "shell": ["bash", "shell"],
            "kubernetes": ["bash", "shell"],
            "docker": ["bash", "shell"],
            "git": ["bash", "shell"],
            "ansible": ["bash", "shell"],
            "jenkins": ["bash", "shell"],
            "html": ["html"],
            "css": ["css"],
            "javascript": ["js", "javascript"],
            "react": ["js", "javascript"],
            "jquery": ["js", "javascript"],
            "java": ["java"],
            "c": ["c"],
            "cpp": ["cpp"],
            "go": ["go"],
            "rust": ["rust"],
            "mysql": ["sql"],
        }
        self.parse_skills = ParseSkills()

    def __parse_code_block(self, step_content: str, language: str) -> list:
        # parse checker content begin ```checker
        code_blocks = step_content.split(f"```{language}")[1:]
        # parse checker content end ```
        code_block_content = [i.split("```")[0] for i in code_blocks]
        return code_block_content

    def add_skills(self, dir_path: str, skilltree: str) -> None:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith("index.json"):
                    index_path = os.path.join(root, file)
                    # read the index.json file
                    with open(index_path, "r") as f:
                        data = json.load(f)
                    steps = data["details"]["steps"]
                    task_type = "ADD"
                    for step in steps:
                        step_text = os.path.join(root, step["text"])
                        skills_original = step.get("skills", [])
                        if skilltree == None:
                            # only sort the skills
                            all_skills = list(set(skills_original))
                            task_type = "SORT"
                        else:
                            # read the step file
                            with open(step_text, "r") as f:
                                step_content = f.read()
                            step_skills = []
                            # parse the code block
                            languages = self.languages[skilltree]
                            for language in languages:
                                code_block_content = self.__parse_code_block(
                                    step_content, language
                                )
                                code_block_content = "\n".join(code_block_content)
                                skills = self.parse_skills.parse(
                                    skilltree, code_block_content
                                )
                                step_skills += skills
                            # update the index.json file
                            all_skills = list(set(skills_original + step_skills))
                        step["skills"] = sorted(all_skills)
                    # update the index.json file
                    with open(index_path, "w") as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)
                    # run prettier
                    os.system(f"prettier --log-level silent --write {index_path}")
                    print(f"[green]→ {task_type} SKILLS:[/] {index_path}")
