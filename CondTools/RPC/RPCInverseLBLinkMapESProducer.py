import FWCore.ParameterSet.Config as cms

def RPCInverseLBLinkMapESProducer(**kwargs):
  mod = cms.ESProducer('RPCInverseLBLinkMapESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
