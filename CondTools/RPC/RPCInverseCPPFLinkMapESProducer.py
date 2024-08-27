import FWCore.ParameterSet.Config as cms

def RPCInverseCPPFLinkMapESProducer(**kwargs):
  mod = cms.ESProducer('RPCInverseCPPFLinkMapESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
