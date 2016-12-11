# Git Hash Check
>Script to check git projects hash build

## How-to

Once you have a project that generate on build a git.properties file.

```
~$ python check.py -a <path_to_jar>
```

And the output will be something similar to

```
git.branch=master
git.commit.id=a70a5917db98176352e5479590e4528756084708
git.commit.id.abbrev=a70a591
git.commit.user.name=Alex Rocha
git.commit.user.email=alex.rochas@yahoo.com.br
git.commit.message.short=Merge pull request #79 in <branch> from develop to master
git.commit.message.full=Merge pull request #79 in <branch> from develop to master

* commit 'd62cd8bdbcdb19d2abba7a179dc99cf5e38ef67f': (183 commits)
  changes for prod deploy
  add product status values
  fix numeric values parsing
  fix conf conflicts
  add new column to audit table
  fix props & config
  fix oracle credentials for pp env
  comment out data contract v20 changes until dhl implement them
  define specific conf files by env
  fix blank values for non-null fields
  fix issue 586
  fix issue 616
  fix issue 614
  fix issue 612
  fix issue 587
  fix issue 606
  update tnsnames.ora
  ...

git.commit.time=1478689677
```

## Release History

* 0.1.0
    * Draft script.

## Roadmap

  * Retrieve more information about the project
  * Format dates
  * Filter important information

## Meta

Alex Rocha - [about.me](http://about.me/alex.rochas)
