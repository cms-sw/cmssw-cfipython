import FWCore.ParameterSet.Config as cms

def L1HfRingEtScaleOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('L1HfRingEtScaleOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
