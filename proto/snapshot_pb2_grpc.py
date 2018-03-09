# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import snapshot_pb2 as snapshot__pb2


class snap_shotStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.add_snap = channel.unary_unary(
        '/snapshot.snap_shot/add_snap',
        request_serializer=snapshot__pb2.image_data.SerializeToString,
        response_deserializer=snapshot__pb2.result.FromString,
        )


class snap_shotServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def add_snap(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_snap_shotServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'add_snap': grpc.unary_unary_rpc_method_handler(
          servicer.add_snap,
          request_deserializer=snapshot__pb2.image_data.FromString,
          response_serializer=snapshot__pb2.result.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'snapshot.snap_shot', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))