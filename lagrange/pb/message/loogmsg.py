from typing import List
from lagrange.utils.binary.protobuf import proto_field, ProtoStruct


class LongMsgContent(ProtoStruct):
    msg_body: List = proto_field(1)  # working


class LongMsgAction(ProtoStruct):
    action_command: str = proto_field(1)
    action_data: LongMsgContent = proto_field(2)


class LongMsgResult(ProtoStruct):
    action: LongMsgAction = proto_field(2)
