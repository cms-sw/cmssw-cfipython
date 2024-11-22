import FWCore.ParameterSet.Config as cms

def RPCInverseCPPFLinkMapESProducer(*args, **kwargs):
  mod = cms.ESProducer('RPCInverseCPPFLinkMapESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
