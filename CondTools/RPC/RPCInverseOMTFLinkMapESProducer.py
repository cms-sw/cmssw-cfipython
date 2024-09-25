import FWCore.ParameterSet.Config as cms

def RPCInverseOMTFLinkMapESProducer(*args, **kwargs):
  mod = cms.ESProducer('RPCInverseOMTFLinkMapESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
