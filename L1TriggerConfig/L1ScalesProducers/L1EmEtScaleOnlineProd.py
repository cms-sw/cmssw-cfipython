import FWCore.ParameterSet.Config as cms

def L1EmEtScaleOnlineProd(**kwargs):
  mod = cms.ESProducer('L1EmEtScaleOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
