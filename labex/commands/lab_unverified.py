import json
from rich import print
from .utils.api import AdminData, UserData
from .utils.auth import AuthGitHub
from github import Github


class LabForTesting:
    def __init__(self) -> None:
        # for labex
        self.__admin_data = AdminData()
        all_paths = UserData().get_all_path()
        self.path_alias = [p["alias"] for p in all_paths["paths"]]
        # for github
        GITHUB_TOKEN = AuthGitHub().read_github_token()
        repo_name = "labex-labs/labs-validation"
        g = Github(login_or_token=GITHUB_TOKEN, retry=10)
        self.repo = g.get_repo(repo_name)

    def __get_labs(self) -> list:
        namespaces = [
            "33fa8aba-d546-42e9-9692-64968aeaf0cc",
            # "df87b950-1f37-4316-bc07-6537a1f2c481",
            # "0537fd91-a50d-4b12-b402-cf6582be4fd4",
        ]
        # get labs
        all_labs = []
        for namespace in namespaces:
            labs = self.__admin_data.get_namespace_labs(namespace)
            print(f"Namespace: {namespace}, Labs: {len(labs)}")
            all_labs.extend(labs)
        # filter labs
        unverified_labs = [lab for lab in all_labs if lab["is_unverified"]]
        verified_labs = [lab for lab in all_labs if not lab["is_unverified"]]
        print(
            f"All Labs: {len(all_labs)}, Unverified Labs: {len(unverified_labs)}, Verified Labs: {len(verified_labs)}"
        )
        return unverified_labs, verified_labs

    def __get_issues_title(self, state: str) -> list:
        issues = self.repo.get_issues(state=state)
        all_issues = []
        for issue in issues:
            all_issues.append(issue.title)
        return list(set(all_issues))

    def __parse_lab(self, lab_data: dict) -> list:
        """Parse lab data

        Args:
            lab_data (dict): {
                                "id": 117029,
                                "namespace": "33fa8aba-d546-42e9-9692-64968aeaf0cc",
                                "path": "ansible/challenge-ansible-command-module",
                                "type": 1,
                                "title": "Ansible Command Module",
                                "difficulty": "Beginner",
                                "time": 15,
                                "fee_type": 2,
                                "pass_user_count": 0,
                                "is_unverified": true
                            }

        Returns:
            list: _description_
        """
        lab_id = lab_data["id"]
        lab_title = lab_data["title"]
        lab_path = lab_data["path"]
        lab_derection = lab_path.split("/")[0]
        if lab_derection in self.path_alias:
            lab_alias = lab_derection
        else:
            lab_alias = "python"
        if lab_data["type"] == 1:
            lab_type = "challenge"
        else:
            lab_type = "lab"
        lab_url = f"https://labex.io/skilltrees/{lab_alias}/labs/{lab_id}"
        return lab_title, lab_path, lab_url, lab_derection, lab_type

    def __create_issue(
        self, lab_title, lab_path, lab_url, lab_derection, lab_type
    ) -> None:
        issue_body = f"""# {lab_title}

## 测试说明

1. 点击 Issue 右侧 Assignees，将测试 Issue 分配给自己，请勿选择已被别人认领的 Issue；
2. 请在 **认领后的 12 小时** 内完成 Issue 所关联的 Lab 测试，超期系统会自动取消认领；
4. 测试完成后，请编辑和补充下方的【测试检查单】和【测试报告】；
5. 测试完成后，请在右侧 Labels 里选择 `verified` 标签标记已完成测试，同时取消默认的 `unverified` 标签。如果相应 lab 存在问题需要修复，则同时添加 `needfix` 标签，如果无问题则添加 `wontfix` 标签；
7. 系统将进行测试完成状态核对，我们会对反馈问题进行修复；

## 测试地址

- 测试地址（右键新标签页面打开，若无法学习请联系我们）：{lab_url}

## 测试检查单

> 请点击复选框，勾选后自动保存。

1. 我以**用户视角**在默认环境中完成了 Lab 的学习，直到最后一步。
   - [ ] 是
2. 我确认此 Lab 存在以下问题：
   - [ ] 检测脚本在用户未操作时可以直接通过；
   - [ ] 检测脚本在操作正确时无法通过；
   - [ ] 检测脚本的提示不够明确和清晰；
   - [ ] 步骤无法走通，内容和代码不明晰，甚至错误；
   - [ ] 存在明显的格式问题；
   - [ ] 无任何上述问题，但我认为此 Lab 用户可以正常学习。
3. 评价此 Lab 的质量：
   - [ ] 我认为此 Lab 的质量不错，建议保留；
   - [ ] 我认为此 Lab 的质量还行，建议修复；
   - [ ] 我认为此 Lab 的质量不佳，建议移除；

## 测试报告

请以评论的方式，将您测试的问题反馈到此 issue 中。

请务必详细描述问题和复现方法，并补充截图（直接粘贴到本评论框）或录屏（可以使用 [芦笋](https://lusun.com) 分享录屏链接）。

问题记录模板可以参考下方，也可以根据需要自定义格式，确保我们不需要多余的沟通就能看懂即可。

- 问题描述：
- 复现方法：
- 截图或录屏：
"""
        # create issue
        issue = self.repo.create_issue(
            title=lab_path,
            body=issue_body,
            labels=["unverified", lab_type, lab_derection],
        )
        print(issue)

    def main(self):
        all_issues = self.__get_issues_title(state="all")
        print(f"All Issues: {len(all_issues)}")
        unverified_labs, verified_labs = self.__get_labs()
        # create issue for new unverified labs
        for lab in unverified_labs:
            try:
                (
                    lab_title,
                    lab_path,
                    lab_url,
                    lab_derection,
                    lab_type,
                ) = self.__parse_lab(lab)
                if lab_path not in all_issues:
                    self.__create_issue(
                        lab_title, lab_path, lab_url, lab_derection, lab_type
                    )
            except Exception as e:
                print(e)
                continue
        # close issue for verified labs without assignees
        open_issues = self.repo.get_issues(state="open")
        verified_labs_path = [lab["path"] for lab in verified_labs]
        close_issue_count = 0
        for issue in open_issues:
            issue_title = issue.title
            issue_assignees = issue.assignees
            if issue_title in verified_labs_path and len(issue_assignees) == 0:
                try:
                    issue.create_comment(
                        "This issue is closed by system, because it is verified."
                    )
                    issue_labels = [label.name for label in issue.labels]
                    issue_labels.remove("unverified")
                    issue_labels.extend(["verified", "wontfix", "autoclosed"])
                    issue.edit(state="closed", labels=issue_labels)
                    print(f"Close Issue: {issue_title}, because it is verified.")
                    close_issue_count += 1
                except Exception as e:
                    print(e)
                    continue
        print(
            f"Open Issues: {open_issues.totalCount}, Auto Close Issues: {close_issue_count}"
        )
