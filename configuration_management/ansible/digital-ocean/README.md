# README
## digital ocean
- https://sendgrid.com/blog/ansible-and-digital-ocean/
### Notes
- do not use ubuntu, it does not come with Python so Andible chokes. Use centos instead.
```
ansible all -m ping -u root --private-key=~/.ssh/id_rsa
```

# installing scala
- https://www.vultr.com/docs/how-to-install-scala-on-centos-7 .- has the correct repo
