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

from .partition_analysis_event import PartitionAnalysisEvent


class PartitionPrimaryMoveAnalysisEvent(PartitionAnalysisEvent):
    """Partition Primary Move Analysis event.

    :param event_instance_id: The identifier for the FabricEvent instance.
    :type event_instance_id: str
    :param category: The category of event.
    :type category: str
    :param time_stamp: The time event was logged.
    :type time_stamp: datetime
    :param has_correlated_events: Shows there is existing related events
     available.
    :type has_correlated_events: bool
    :param kind: Constant filled by server.
    :type kind: str
    :param partition_id: An internal ID used by Service Fabric to uniquely
     identify a partition. This is a randomly generated GUID when the service
     was created. The partition ID is unique and does not change for the
     lifetime of the service. If the same service was deleted and recreated the
     IDs of its partitions would be different.
    :type partition_id: str
    :param metadata: Metadata about an Analysis Event.
    :type metadata: ~azure.servicefabric.models.AnalysisEventMetadata
    :param when_move_completed: Time when the move was completed.
    :type when_move_completed: datetime
    :param previous_node: The name of a Service Fabric node.
    :type previous_node: str
    :param current_node: The name of a Service Fabric node.
    :type current_node: str
    :param move_reason: Move reason.
    :type move_reason: str
    :param relevant_traces: Relevant traces.
    :type relevant_traces: str
    """

    _validation = {
        'event_instance_id': {'required': True},
        'time_stamp': {'required': True},
        'kind': {'required': True},
        'partition_id': {'required': True},
        'metadata': {'required': True},
        'when_move_completed': {'required': True},
        'previous_node': {'required': True},
        'current_node': {'required': True},
        'move_reason': {'required': True},
        'relevant_traces': {'required': True},
    }

    _attribute_map = {
        'event_instance_id': {'key': 'EventInstanceId', 'type': 'str'},
        'category': {'key': 'Category', 'type': 'str'},
        'time_stamp': {'key': 'TimeStamp', 'type': 'iso-8601'},
        'has_correlated_events': {'key': 'HasCorrelatedEvents', 'type': 'bool'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
        'metadata': {'key': 'Metadata', 'type': 'AnalysisEventMetadata'},
        'when_move_completed': {'key': 'WhenMoveCompleted', 'type': 'iso-8601'},
        'previous_node': {'key': 'PreviousNode', 'type': 'str'},
        'current_node': {'key': 'CurrentNode', 'type': 'str'},
        'move_reason': {'key': 'MoveReason', 'type': 'str'},
        'relevant_traces': {'key': 'RelevantTraces', 'type': 'str'},
    }

    def __init__(self, event_instance_id, time_stamp, partition_id, metadata, when_move_completed, previous_node, current_node, move_reason, relevant_traces, category=None, has_correlated_events=None):
        super(PartitionPrimaryMoveAnalysisEvent, self).__init__(event_instance_id=event_instance_id, category=category, time_stamp=time_stamp, has_correlated_events=has_correlated_events, partition_id=partition_id, metadata=metadata)
        self.when_move_completed = when_move_completed
        self.previous_node = previous_node
        self.current_node = current_node
        self.move_reason = move_reason
        self.relevant_traces = relevant_traces
        self.kind = 'PartitionPrimaryMoveAnalysis'
