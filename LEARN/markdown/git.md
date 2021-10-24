# Notes about git
- From tutorial at lynda.com

## git ls-tree
```
>git ls-tree HEAD
040000 tree 61335b3219e3a7f31a4fe8950613010b1231a1c0	Automator
040000 tree a28aa293b859aebcc0d7c85d128fa1ea8c917942	LearningCocoa
100644 blob 7d98d2c225dbb974ac22d1c0dd850aa71e4454ee	README.md
040000 tree 3b6ee53b78e4726edf8a2b8f5c3dbe5fb5db67b7	ansible
040000 tree 1592bf0bcfd971cbcb07a3af4ebabe5f95886da5	bash
040000 tree 5d583358958525916a629c7e9399d7a86978444a	c

>git ls-tree HEAD README.md
100644 blob 7d98d2c225dbb974ac22d1c0dd850aa71e4454ee	README.md
```

## git log
```
>git log --oneline -4
8ad00b5 added scala-droplet and updated readme
c815422 added scala-droplet and updated readme
aa577a7 updated host file;updated for scala
b745e95 initial.

>git log --oneline --since="2016"
8ad00b5 added scala-droplet and updated readme
c815422 added scala-droplet and updated readme
aa577a7 updated host file;updated for scala
b745e95 initial.
d382e53 Removed untracted files from cache.
69ed2a0 deleted git links notes
89cab4e rm gitignore
57d3d70 Merge branch 'master' of github.com:mayelespino/code
dd26680 updates.
5e61c5c Update README.md
f4b9681 renamed
3c75d8b init
f654634 added .gitignore
cfbf4bd renamed.
4e3267e deleted.
9315ad5 deleted stuff.
82d0f88 update
b91a877 catchint up.
07d6dc2 initial
d732bad initial

>git log --oneline d382e53..8ad00b5
8ad00b5 added scala-droplet and updated readme
c815422 added scala-droplet and updated readme
aa577a7 updated host file;updated for scala
b745e95 initial.

>git log --grep="update" --oneline
8ad00b5 added scala-droplet and updated readme
c815422 added scala-droplet and updated readme
aa577a7 updated host file;updated for scala
dd26680 updates.
82d0f88 update
a979fff update
afbe7b3 updated.
d75b4f9 update
2dbab31 updated links.txt
a431c2b update code examples.
7b2d0cc updated yahoo int solve.
444b3e4 updated yahoo int solve.


>git log -p README.md
commit 5e61c5c3f7a29d15cc9c7de359a840cfcd346851
Author: mayel espino <mayel.espino@gmail.com>
Date:   Sun Mar 19 00:00:44 2017 -0700

    Update README.md

diff --git a/README.md b/README.md
index 199fb9e..7d98d2c 100644
--- a/README.md
+++ b/README.md
@@ -1,9 +1,4 @@
 # code
-Code examples for tutorial purposes. In some cases I based my self on code I found online, when this was the case: I tried to do my best to mention where I got these examples.
+Code examples for tutorial purposes. In some cases I based my self on code I found online, when this was the case: I tried to do my best to mention where I got these example (give credit where credit is due).

-# Vagrant
-I used Vagrant VMs to create disposable and reproducible development environments. I also wanted to avoid installing stuff on my laptop.
-
-## Vagrant file configuration and provisioning
-* http://www.sitepoint.com/vagrantfile-explained-setting-provisioning-shell/
-* https://www.vagrantup.com/docs/provisioning/chef_solo.html
+Please visit the wiki: https://github.com/mayelespino/code/wiki

commit afbe7b322f050404da189152ce1e4ebbd35ba43a
Author: mayel espino <mayel.espino@gmail.com>
Date:   Thu Dec 1 21:48:40 2016 -0800

    updated.

diff --git a/README.md b/README.md
index cac1c30..199fb9e 100644
--- a/README.md
+++ b/README.md
@@ -1,8 +1,6 @@
 # code
 Code examples for tutorial purposes. In some cases I based my self on code I found online, when this was the case: I tried to do my best to mention where I got these examples.
-- c
-- java
--
+
 # Vagrant
 I used Vagrant VMs to create disposable and reproducible development environments. I also wanted to avoid installing stuff on my laptop.

 >git log --format=fuller README.md
commit 5e61c5c3f7a29d15cc9c7de359a840cfcd346851
Author:     mayel espino <mayel.espino@gmail.com>
AuthorDate: Sun Mar 19 00:00:44 2017 -0700
Commit:     GitHub <noreply@github.com>
CommitDate: Sun Mar 19 00:00:44 2017 -0700

    Update README.md

commit afbe7b322f050404da189152ce1e4ebbd35ba43a
Author:     mayel espino <mayel.espino@gmail.com>
AuthorDate: Thu Dec 1 21:48:40 2016 -0800
Commit:     GitHub <noreply@github.com>
CommitDate: Thu Dec 1 21:48:40 2016 -0800

    updated.

>git log --format=short README.md
commit 5e61c5c3f7a29d15cc9c7de359a840cfcd346851
Author: mayel espino <mayel.espino@gmail.com>

    Update README.md

commit afbe7b322f050404da189152ce1e4ebbd35ba43a
Author: mayel espino <mayel.espino@gmail.com>

    updated.


>git log --stat --summary README.md
commit 5e61c5c3f7a29d15cc9c7de359a840cfcd346851
Author: mayel espino <mayel.espino@gmail.com>
Date:   Sun Mar 19 00:00:44 2017 -0700

    Update README.md

 README.md | 9 ++-------
 1 file changed, 2 insertions(+), 7 deletions(-)

commit afbe7b322f050404da189152ce1e4ebbd35ba43a
Author: mayel espino <mayel.espino@gmail.com>
Date:   Thu Dec 1 21:48:40 2016 -0800

    updated.

 README.md | 4 +---
 1 file changed, 1 insertion(+), 3 deletions(-)

commit fafcf68ce87249a71b7922d49518a55db5bee0a2
Author: Mayel Espino <mayel.espino@gmail.com>
Date:   Wed Mar 2 20:30:37 2016 -0800


>git log --graph
* commit 8ad00b588b368cdd4877e269927db140db8cf5f3
| Author: Mayel Espino <mayel.espino@gmail.com>
| Date:   Sat Apr 8 22:28:26 2017 -0700
|
|     added scala-droplet and updated readme
|
* commit 89cab4e67b96a5b15a66ff426913deb65ba7ebb7
| Author: Mayel Espino <mayel.espino@gmail.com>
| Date:   Sun Mar 19 20:47:53 2017 -0700
|
|     rm gitignore
|
*   commit 57d3d70648cc8174addad157a2455f2a6fe9a445
|\  Merge: dd26680 5e61c5c
| | Author: Mayel Espino <mayel.espino@gmail.com>
| | Date:   Sun Mar 19 20:36:14 2017 -0700
| |
:
```

## Git show
```
>git show 57d3d70648cc8174addad157a2455f2a6fe9a445
commit 57d3d70648cc8174addad157a2455f2a6fe9a445
Merge: dd26680 5e61c5c
Author: Mayel Espino <mayel.espino@gmail.com>
Date:   Sun Mar 19 20:36:14 2017 -0700

    Merge branch 'master' of github.com:mayelespino/code

[0|21:38:21|~/Repos/code]

```
## git diff
```
>git diff 89cab4e67b96a5b15a66ff426913deb65ba7ebb7..HEAD
diff --git a/.DS_Store b/.DS_Store
deleted file mode 100644
index f5c4661..0000000
Binary files a/.DS_Store and /dev/null differ
diff --git a/ansible/digital-ocean/README.md b/ansible/digital-ocean/README.md
index b107339..a804102 100644
--- a/ansible/digital-ocean/README.md
+++ b/ansible/digital-ocean/README.md
@@ -1,6 +1,11 @@
 # README
-https://sendgrid.com/blog/ansible-and-digital-ocean/
+## digital ocean
+- https://sendgrid.com/blog/ansible-and-digital-ocean/
+### Notes
+- do not use ubuntu, it does not come with Python so Andible chokes. Use centos instead.
+ansible all -m ping -u root --private-key=~/.ssh/id_rsa


>git diff -w 89cab4e67b96a5b15a66ff426913deb65ba7ebb7..HEAD (ignore white space)

>git diff -b (ignore space)

>git diff --color-words branch1..branch2
```
## Git alias
- https://githowto.com/aliases
```
git config --global alias.co checkout
```
