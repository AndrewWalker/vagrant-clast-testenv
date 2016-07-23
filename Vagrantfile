# vi: set ft=ruby 

servers=[
    {
        :hostname => "llvm38",
        :provags => "'3.8'"
    },
    {
        :hostname => "llvm39",
        :provags => "'3.9'"
    },
    {
        :hostname => "llvm40",
        :provags => "'4.0'"
    }
]

Vagrant.configure(2) do |config|
  servers.each do |machine|
    config.vm.define machine[:hostname] do |node|
      node.vm.box = "ubuntu/trusty64"
      node.ssh.forward_agent = true
      if Vagrant.has_plugin?("vagrant-cachier")
        node.cache.scope = :box
      end
      node.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "6144"]
        vb.customize ["modifyvm", :id, "--cpus", "2"]   
      end  
      node.vm.provision "shell" do |s|
        s.inline = "/vagrant/provision $1"
        #s.inline = "echo $1"
        s.args   = machine[:provags]
      end
    end
  end
end
