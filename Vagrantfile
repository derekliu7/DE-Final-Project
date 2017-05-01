# Require the AWS provider plugin
require 'vagrant-aws'

# Require YAML module
require 'yaml'

# Read YAML file with box details
cred = YAML.load_file(ENV['HOME'] + '/.ssh/aws_cred.yml')

# Create and configure the AWS instance(s)
Vagrant.configure('2') do |config|

  # Use dummy AWS box
  config.vm.box = 'dummy'

  config.vm.provision :shell, path: "bootstrap.sh"

  # Specify VirtualBox provider configuration
  config.vm.provider 'virtualbox' do |vb, override|
    override.vm.box = 'ubuntu/xenial64'
  end

  # Specify AWS provider configuration
  config.vm.provider :aws do |aws, override|

    # Read AWS authentication information from environment variables
    aws.access_key_id = cred['aws']['aws_access_key_id']
    aws.secret_access_key = cred['aws']['aws_secret_access_key']

    # Specify SSH keypair to use
    aws.keypair_name = 'newkey'

    # Specify region, AMI ID, and security group(s)
    aws.instance_type = 't2.micro'
    aws.region = 'us-east-1'
    aws.ami = 'ami-f4cc1de2'
    aws.security_groups = ['launch-wizard-2']

    # Specify username and private key path
    override.ssh.username = 'ubuntu'
    override.ssh.private_key_path = '/Users/DL/.ssh/newkey.pem'
  end
end
