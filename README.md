# 1326PokerBot

1. Repository
   * This is basically your project folder. All the files that everyone will use will fall within this
2. Branch
   * This is what we'll use so that we don't upload bad code to the main and break everything. When we want to code something, we'll make a new branch, call it MyFeature, and then make and save changes in here. We can do this with `git checkout -b <my feature>` and `git push --set-upstream origin <my feature>`.
   * While we make changes in here, other people might be making changes in their branches, and eventually merging them back into main.
   * Making Changes
       * While we're in our branch, we can make as many changes as we'd like. If you're on VSCode, you can see your current branch in the bottom left and your changes as the third symbol on the left wall.
       * Once we're happy with our changes, we can use the terminal to cd to our current working directory. Use `git status` to see all the modified files that haven't been committed. Then use `git add <files>` to add files individually, or `git add .` to add all files in the directory.
       * After this, we can write our commit message using `git commit -m "<my feature>: <what the feature is doing>"`
       * Then we push it to the branch with `git push`!
3. Merging (aka pulling)
   * While we were making changes in our own branch, someone else might have finished whatever they were doing in their branch and merged it with main, so we need to make sure our version of main is up-to-date for when we try to merge our branch.
   * To do that, we'll have to switch to the main branch with `git checkout main`, then use `git pull` to update the main branch.
   * We can then merge our branch into our local main with `git merge <my feature>` while we are in our main branch (this can be double-checked with `git branch`).
   * After this, we can finalize our branch by pushing with `git push origin <my feature>`
