import FWCore.ParameterSet.Config as cms

def DTTFMasksOnlineProd(**kwargs):
  mod = cms.ESProducer('DTTFMasksOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
