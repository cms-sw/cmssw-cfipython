import FWCore.ParameterSet.Config as cms

def RPCInverseTwinMuxLinkMapESProducer(*args, **kwargs):
  mod = cms.ESProducer('RPCInverseTwinMuxLinkMapESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
