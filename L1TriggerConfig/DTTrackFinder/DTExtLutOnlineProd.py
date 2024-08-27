import FWCore.ParameterSet.Config as cms

def DTExtLutOnlineProd(**kwargs):
  mod = cms.ESProducer('DTExtLutOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
