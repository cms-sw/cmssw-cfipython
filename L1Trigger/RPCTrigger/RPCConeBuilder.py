import FWCore.ParameterSet.Config as cms

def RPCConeBuilder(**kwargs):
  mod = cms.ESProducer('RPCConeBuilder',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
