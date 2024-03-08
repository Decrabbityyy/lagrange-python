from lagrange.pb.message.rich_text import Elems
from lagrange.utils.binary.protobuf import ProtoStruct, ProtoField


class GetGrpMsgReqBody(ProtoStruct):
    grp_id: int = ProtoField(1)
    start_seq: int = ProtoField(2)
    end_seq: int = ProtoField(3)


class PBGetGrpMsgRequest(ProtoStruct):
    body: GetGrpMsgReqBody = ProtoField(1)
    direction: bool = ProtoField(2, True)

    @classmethod
    def build(cls, grp_id: int, start_seq: int, end_seq: int, direction=True) -> 'PBGetGrpMsgRequest':
        return cls(body=GetGrpMsgReqBody(grp_id=grp_id, start_seq=start_seq, end_seq=end_seq), direction=direction)


class RecallRequestF3(ProtoStruct):
    seq: int = ProtoField(1)
    # rand: int = ProtoField(2)
    field3: int = ProtoField(3, 0)


class PBGroupRecallRequest(ProtoStruct):
    type: int = ProtoField(1, 1)
    grp_id: int = ProtoField(2)
    field3: RecallRequestF3 = ProtoField(3)
    field4: dict = ProtoField(4, {1: 0})

    @classmethod
    def build(cls, grp_id: int, seq: int) -> 'PBGroupRecallRequest':
        return PBGroupRecallRequest(
            grp_id=grp_id,
            field3=RecallRequestF3(
                seq=seq
            )
        )


class RenameRequestF2(ProtoStruct):
    name: str = ProtoField(3)


class PBGroupRenameRequest(ProtoStruct):
    grp_id: int = ProtoField(1)
    rename_f2: RenameRequestF2 = ProtoField(2)

    @classmethod
    def build(cls, grp_id: int, name: str) -> 'PBGroupRenameRequest':
        return cls(grp_id=grp_id, rename_f2=RenameRequestF2(name=name))


class RenameMemberRequestF3(ProtoStruct):
    uid: str = ProtoField(1)
    name: str = ProtoField(8)


class PBRenameMemberRequest(ProtoStruct):
    grp_id: int = ProtoField(1)
    rename_f3: RenameMemberRequestF3 = ProtoField(3)

    @classmethod
    def build(cls, grp_id: int, target_uid: str, name: str) -> 'PBRenameMemberRequest':
        return cls(grp_id=grp_id, rename_f3=RenameMemberRequestF3(uid=target_uid, name=name))


class PBLeaveGroupRequest(ProtoStruct):
    grp_id: int = ProtoField(1)

    @classmethod
    def build(cls, grp_id: int) -> 'PBLeaveGroupRequest':
        return cls(grp_id=grp_id)


class GetGrpMsgRspBody(ProtoStruct):
    grp_id: int = ProtoField(3)
    start_seq: int = ProtoField(4)
    end_seq: int = ProtoField(5)
    elems: list[bytes] = ProtoField(6)


class GetGrpMsgRsp(ProtoStruct):
    body: GetGrpMsgRspBody = ProtoField(3)
