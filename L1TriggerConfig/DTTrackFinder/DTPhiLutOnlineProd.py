import FWCore.ParameterSet.Config as cms

def DTPhiLutOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('DTPhiLutOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
