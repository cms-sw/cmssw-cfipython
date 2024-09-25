import FWCore.ParameterSet.Config as cms

def DTTFMasksOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('DTTFMasksOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
