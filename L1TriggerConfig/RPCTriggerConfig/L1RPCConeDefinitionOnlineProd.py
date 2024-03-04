import FWCore.ParameterSet.Config as cms

def L1RPCConeDefinitionOnlineProd(**kwargs):
  mod = cms.ESProducer('L1RPCConeDefinitionOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
