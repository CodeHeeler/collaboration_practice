# Collaboration, Branching, and Merging Practice in Git

First, be sure you're added as a collaborator or use pull requests.  For this walkthrough, we'll be going the collaborator route.  The same applies for Trello so that you can alert your team as to what feature or bug you are working on presently.

1. Clone the GitHub repository for your team's project and set up your environment.

2. Based on the feature you've chosen to work on, create an appropriately named branch and swap to it (for this example, Feature 42).
  1. This can be done in one step:
  ```
  $ git checkout -b feature42
  ```
  2. Or in two steps:
  ```
  $ git branch feature42
  $ git checkout feature42
  ```

3. Implement your function, creating, editing, and testing files and continue to commit regularly to your new branch, and even your own remote.

4. At any time, you can checkout a different branch to take on something of higher priority and come back to this one, but once you are finished, it is time to merge back with master.

5. Swap back to master
```
$ git checkout master
```

6. Attempt to merge--sometimes if there are no other changes, the master will be "fast forwarded" to include the new code, and sometimes auto-merge takes care of it for you.
```
$ git merge feature42
```

7. If your merge failed, take a look at which files need attention.
```
$ git status
```

8. Go to each of those files and look through them for the word HEAD added along with some lines demarcating two sections, the top being your new material, the bottom being what is currently in master.
  1. Choose which you would like to keep, or make edits to conserve both or consult your team, then delete the conflicting material as well as all auto-generated lines.
  2. Now you may add your changes.
  ```
  $ git add
  ```
  3. A commit message has been generated for you with info about the merge, so commit this way:
  ```
  $ git commit
  ```
  Then either add additional information to the file that comes up in vim or another text editor or type `:q` to quit the editor.

9. Now push and if you have taken care of all merge conflicts, you will be up to date.

10. To keep the work are clean, you may now want to delete your old branch.  Some companies prefer that you leave them around for a while and then have a purge of old files at a later date. Check what is common practice for the codebase you're working on, and when you're ready to delete your old branch:
```
$ git branch -d feature42
```
And then remove the remote for it if you were using one:
```
$ git push origin :feature42
```


## Thanks for following along!

### References:
This walkthrough was based off the following tutorial:
https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

And advice from:
  * Jon Alligood
  * Dave Masog

And put together by:
  * Dana Walker
