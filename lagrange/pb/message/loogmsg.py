from typing import List, Optional
from lagrange.utils.binary.protobuf import proto_field, ProtoStruct

"""
Copy from LagrangeDev/Lagrange.Core
"""


class ResponseForward(ProtoStruct):
    friend_name: Optional[str] = proto_field(6, default=None)


class ResponseGrp(ProtoStruct):
    groupUin: int = proto_field(1)
    member_name: str = proto_field(4)
    group_name: str = proto_field(7)


class ResponseHead(ProtoStruct):
    from_uin: int = proto_field(1)
    from_uid: Optional[str] = proto_field(2, default=None)
    type: int = proto_field(3)
    sig_map: str = proto_field(4)
    to_uin: int = proto_field(5)
    to_uid: Optional[str] = proto_field(6, default=None)
    forward: Optional[ResponseForward] = proto_field(7, default=None)
    grp: Optional[ResponseGrp] = proto_field(8, default=None)


class ForwardHead(ProtoStruct):
    f1: Optional[int] = proto_field(1, default=None)  # 0
    f2: Optional[int] = proto_field(2, default=None)  # 0
    f3: Optional[int] = proto_field(3, default=None)  # for friend: 2, for group: null
    unknown_b64: Optional[str] = proto_field(4, default=None)
    avatar: Optional[str] = proto_field(5, default=None)


class ContentHead(ProtoStruct):
    type: int = proto_field(1)
    sub_type: Optional[int] = proto_field(2, default=None)
    div_seq: Optional[int] = proto_field(3, default=None)
    msg_id: Optional[int] = proto_field(4, default=None)
    timestamp: Optional[int] = proto_field(5, default=None)
    msg_flag: Optional[int] = proto_field(6, default=None)
    f7: Optional[int] = proto_field(7, default=None)
    f8: Optional[int] = proto_field(8, default=None)
    f9: Optional[int] = proto_field(9, default=None)
    new_id: Optional[int] = proto_field(12, default=None)
    forward: Optional[ForwardHead] = proto_field(15, default=None)


class MessageBody(ProtoStruct):
    rich_text: Optional[str] = proto_field(1)
    msg_content: Optional[bytes] = proto_field(
        2, default=None
    )  # Offline file is now put here(?
    msg_encrypt_content: Optional[bytes] = proto_field(3, default=None)


class PushMsgBody(ProtoStruct):
    response_head: ResponseHead = proto_field(1)
    content_head: ContentHead = proto_field(2)
    body: Optional[MessageBody] = proto_field(3, default=None)


class LongMsgContent(ProtoStruct):
    msg_body: List[PushMsgBody] = proto_field(1)  # working


class LongMsgAction(ProtoStruct):
    action_command: str = proto_field(1)
    action_data: LongMsgContent = proto_field(2)


class LongMsgResult(ProtoStruct):
    action: LongMsgAction = proto_field(2)
