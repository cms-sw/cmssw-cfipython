import FWCore.ParameterSet.Config as cms

def RPCInverseOMTFLinkMapESProducer(**kwargs):
  mod = cms.ESProducer('RPCInverseOMTFLinkMapESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
