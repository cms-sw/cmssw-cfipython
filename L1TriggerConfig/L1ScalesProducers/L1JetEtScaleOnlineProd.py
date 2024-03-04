import FWCore.ParameterSet.Config as cms

def L1JetEtScaleOnlineProd(**kwargs):
  mod = cms.ESProducer('L1JetEtScaleOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
