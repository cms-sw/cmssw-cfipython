import FWCore.ParameterSet.Config as cms

def L1RCTParametersOnlineProd(**kwargs):
  mod = cms.ESProducer('L1RCTParametersOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
