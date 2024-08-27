import FWCore.ParameterSet.Config as cms

def L1RPCHsbConfigOnlineProd(**kwargs):
  mod = cms.ESProducer('L1RPCHsbConfigOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
