import FWCore.ParameterSet.Config as cms

def L1EmEtScaleOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('L1EmEtScaleOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
