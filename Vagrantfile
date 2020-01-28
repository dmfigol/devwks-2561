Vagrant.configure("2") do |config|
  config.vm.box = "iosxe/16.09.01"
  # IOS XE 16.7+ requires virtio for the network adapters.
  config.vm.network :private_network, virtualbox__intnet: "link1", auto_config: false, nic_type: "virtio"
  config.vm.network :private_network, virtualbox__intnet: "link2", auto_config: false, nic_type: "virtio"

end
