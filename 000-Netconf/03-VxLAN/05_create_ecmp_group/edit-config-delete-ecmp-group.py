from ncclient import manager
import ncclient
import xml.etree.ElementTree as ET

host = "192.168.1.1"
username="netconfuser"
password="netconfuser"

config_next_hop_xml="""
  <config>
      <capable-switch xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:onf:of111:config:yang">
        <ofdpa10:next-hop xc:operation="delete" xmlns:ofdpa10="urn:bcm:ofdpa10:accton01">
          <ofdpa10:id>10</ofdpa10:id>
          <ofdpa10:dest-mac>01:00:5E:00:22:33</ofdpa10:dest-mac>
          <ofdpa10:phy-port>1</ofdpa10:phy-port>
          <ofdpa10:vid>4093</ofdpa10:vid>
        </ofdpa10:next-hop>
      </of11-config:capable-switch>
  </config>
  """
  
config_xml="""
  <config>
      <capable-switch xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:onf:of111:config:yang">
        <ofdpa10:ecmp xc:operation="delete" xmlns:ofdpa10="urn:bcm:ofdpa10:accton01">
          <ofdpa10:id>10</ofdpa10:id>
          <ofdpa10:nexthop-id>10</ofdpa10:nexthop-id>
        </ofdpa10:ecmp>
      </of11-config:capable-switch>
  </config>
  """
  
with manager.connect_ssh(host=host, port=830, username=username, password=password, hostkey_verify=False ) as m:
    print "Delete ECMP group"
    print m.edit_config(target='running', 
                      config=config_xml, 
                      default_operation='delete', 
                      error_option='stop-on-error')

    print "Delete NextHop"
    print m.edit_config(target='running', 
                      config=config_next_hop_xml, 
                      default_operation='delete', 
                      error_option='stop-on-error')

    print m.get_config(source='running').data_xml
