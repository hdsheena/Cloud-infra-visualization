from azure.mgmt.network import NetworkManagementClient
from lxml.etree import Element, SubElement, tostring
import uuid

def handle_virtual_network(resource, rg, network_client, root_element, resource_node_ids):
    # Get the Virtual Network
    virtual_network = network_client.virtual_networks.get(rg.name, resource.name)
    
    print(f"Added Virtual Network {virtual_network.name}")
    virtual_network_id = f"{virtual_network.name}_{uuid.uuid4()}"
    resource_node_ids[virtual_network_id] = virtual_network_id  # Use the Virtual Network name as the key
    virtual_network_node = SubElement(root_element, 'mxCell', {'id': virtual_network_id, 'value': virtual_network.name, 'vertex': '1', 'parent': '1'})
    virtual_network_node.append(Element('mxGeometry', {'width': '80', 'height': '30', 'as': 'geometry'}))
    
    # Call the new function to handle subnets
    handle_subnets(virtual_network, virtual_network_id, root_element, resource_node_ids)

    return root_element, resource_node_ids

def handle_subnets(virtual_network, parent_id, root_element, resource_node_ids):
    for subnet in virtual_network.subnets:
        print(f"Added Subnet {subnet.name}")
        subnet_id = f"{subnet.name}_{uuid.uuid4()}"
        resource_node_ids[subnet_id] = subnet_id  # Use the Subnet name as the key
        subnet_node = SubElement(root_element, 'mxCell', {'id': subnet_id, 'value': subnet.name, 'vertex': '1', 'parent': parent_id})
        subnet_node.append(Element('mxGeometry', {'width': '80', 'height': '30', 'as': 'geometry'}))

        # Link the Subnet to the Virtual Network
        link_vnet_to_subnet(parent_id, subnet_id, root_element)

def link_vnet_to_subnet(vnet_id, subnet_id, root_element):
    print(f"Linked VNet {vnet_id} to Subnet {subnet_id}")
    edge = SubElement(root_element, 'mxCell', {'id': f'{vnet_id}-{subnet_id}', 'value': '', 'edge': '1', 'source': vnet_id, 'target': subnet_id, 'parent': '1'})
    edge.append(Element('mxGeometry', {'relative': '1', 'as': 'geometry'}))