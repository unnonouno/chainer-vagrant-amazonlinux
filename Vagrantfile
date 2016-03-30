# coding: utf-8
# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'yaml'

ec2_config = YAML.load_file('config.yml')

Vagrant.configure(2) do |config|
  config.vm.box = "dummy"
  config.vm.synced_folder ".", "/vagrant", type: "rsync",
                          rsync__exclude: [".git/", "config.yml"]

  config.vm.provider :aws do |aws, override|
    aws.access_key_id = ec2_config["access_key_id"]
    aws.secret_access_key = ec2_config["secret_access_key"]
    aws.keypair_name = ec2_config["keypair_name"]

    aws.ami = "ami-315f4850"
    aws.instance_type = "g2.2xlarge"
    aws.security_groups = ec2_config["security_groups"]
    aws.region = "us-west-2"

    override.ssh.username = "ec2-user"
    override.ssh.private_key_path = ec2_config["private_key_path"]
    override.ssh.pty = true
  end

  config.vm.provision :fabric do |fabric|
    fabric.fabfile_path = "./fabfile.py"
    fabric.tasks = ["install_chainer"]
  end
end
