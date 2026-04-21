
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.addresses import IPAddr

log = core.getLogger()

class DynamicBlocking (object):
    def __init__ (self):
        core.openflow.addListeners(self)
        self.blocked_ips = set()
        log.info("Dynamic Blocking System Initialized")

    def block_host(self, ip_str):
        """Adds an IP to the block list and clears existing flows"""
        self.blocked_ips.add(IPAddr(ip_str))
        log.info("Host %s has been dynamically blocked.", ip_str)
        
        # Clear current flow table to enforce new policy immediately
        for connection in core.openflow.connections:
            connection.send(of.ofp_flow_mod(command=of.OFPFC_DELETE))

    def _handle_PacketIn (self, event):
        packet = event.parsed
        if not packet.parsed:
            return

        ip_packet = packet.find('ipv4')
        
        if ip_packet:
            # Drop traffic if source or destination IP is blocked [cite: 10]
            if ip_packet.srcip in self.blocked_ips or ip_packet.dstip in self.blocked_ips:
                return 

        # Standard Learning Switch logic for authorized traffic
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
        event.connection.send(msg)

def launch ():
    """Registers the component to POX core"""
    core.registerNew(DynamicBlocking)
