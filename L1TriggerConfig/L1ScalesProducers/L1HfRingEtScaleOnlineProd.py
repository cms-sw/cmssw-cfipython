import FWCore.ParameterSet.Config as cms

def L1HfRingEtScaleOnlineProd(**kwargs):
  mod = cms.ESProducer('L1HfRingEtScaleOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
