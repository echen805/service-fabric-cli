# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ClusterHealthChunkQueryDescription(Model):
    """The cluster health chunk query description, which can specify the health
    policies to evaluate cluster health and very expressive filters to select
    which cluster entities to include in response.

    :param node_filters: Defines a list of filters that specify which nodes to
     be included in the returned cluster health chunk.
     If no filters are specified, no nodes are returned. All the nodes are used
     to evaluate the cluster's aggregated health state, regardless of the input
     filters.
     The cluster health chunk query may specify multiple node filters.
     For example, it can specify a filter to return all nodes with health state
     Error and another filter to always include a node identified by its
     NodeName.
    :type node_filters:
     list[~azure.servicefabric.models.NodeHealthStateFilter]
    :param application_filters: Defines a list of filters that specify which
     applications to be included in the returned cluster health chunk.
     If no filters are specified, no applications are returned. All the
     applications are used to evaluate the cluster's aggregated health state,
     regardless of the input filters.
     The cluster health chunk query may specify multiple application filters.
     For example, it can specify a filter to return all applications with
     health state Error and another filter to always include applications of a
     specified application type.
    :type application_filters:
     list[~azure.servicefabric.models.ApplicationHealthStateFilter]
    :param cluster_health_policy: Defines a health policy used to evaluate the
     health of the cluster or of a cluster node.
    :type cluster_health_policy:
     ~azure.servicefabric.models.ClusterHealthPolicy
    :param application_health_policies: Defines the application health policy
     map used to evaluate the health of an application or one of its children
     entities.
    :type application_health_policies:
     ~azure.servicefabric.models.ApplicationHealthPolicies
    """

    _attribute_map = {
        'node_filters': {'key': 'NodeFilters', 'type': '[NodeHealthStateFilter]'},
        'application_filters': {'key': 'ApplicationFilters', 'type': '[ApplicationHealthStateFilter]'},
        'cluster_health_policy': {'key': 'ClusterHealthPolicy', 'type': 'ClusterHealthPolicy'},
        'application_health_policies': {'key': 'ApplicationHealthPolicies', 'type': 'ApplicationHealthPolicies'},
    }

    def __init__(self, node_filters=None, application_filters=None, cluster_health_policy=None, application_health_policies=None):
        super(ClusterHealthChunkQueryDescription, self).__init__()
        self.node_filters = node_filters
        self.application_filters = application_filters
        self.cluster_health_policy = cluster_health_policy
        self.application_health_policies = application_health_policies
