from github import Github
from flask import Flask, render_template, request


g = Github()

app = Flask(__name__)
app.debug= True

@app.route('/', methods=['GET', 'POST'])

def main():
    repoName = ''
    issue = ""
    issueListFull = []
    issueListTop10 = []
    badRepo = ""

    if request.method == 'POST':
            repoName = request.form.get('repo')
            repo = g.get_repo(repoName)
            try:
                if repo:
                    # continue looking up the issues
                    for issue in repo.get_issues():
                        issueListFull.append(issue.title)
                        issueListTop10 = issueListFull[:10]
            except:
                badRepo = "Sorry, that does not appear to be a valid Github repository."

    return render_template('index.html', repoName=repoName, issueListTop10=issueListTop10, badRepo=badRepo)

if __name__ == "__main__":
    app.run()
