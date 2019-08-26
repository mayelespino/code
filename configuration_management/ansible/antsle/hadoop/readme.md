# Hadoop

## Links
- [Single node cluster](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html)
- [Install Hadoop on single node](https://www.tecmint.com/install-configure-apache-hadoop-centos-7/)
- https://hostpresto.com/community/tutorials/how-to-install-apache-hadoop-on-a-single-node-on-centos-7/
- [Ansible playbook to install hadoop](http://whatizee.blogspot.com/2015/05/ansible-playbook-setup-hadoop-cdh5.html)

## changing passwords using Ansbible
- [Chaging password](https://stackoverflow.com/questions/19292899/creating-a-new-user-and-password-with-ansible)
```
How to create encrypted password for passing to password var to Ansible user task (from @Brendan Wood's comment):

openssl passwd -salt 'some_plain_salt' -1 'some_plain_pass'

```
