$script = <<SCRIPT
sudo apt-get update
sudo apt-get install python3-setuptools
sudo apt-get install -y python3.5-dev
sudo easy_install3 pip
sudo pip3 install nose
sudo apt-get install -y python3.5-dev
sudo apt-get install -y redis-server
add-apt-repository ppa:openjdk-r/ppa -y
apt-get update
echo "\n----- Java 8 ------\n"
apt-get -y install apache2 openjdk-8-jdk
update-alternatives --config java
sudo apt-get install -y python2.7-dev
SCRIPT

Vagrant.configure(2) do |config|
  config.vm.box = "bento/ubuntu-16.04"
  config.vm.provision "shell", inline: $script
  config.vm.network "forwarded_port", guest: 5000, host: 5000
end