import FWCore.ParameterSet.Config as cms

def RPCInverseTwinMuxLinkMapESProducer(**kwargs):
  mod = cms.ESProducer('RPCInverseTwinMuxLinkMapESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
