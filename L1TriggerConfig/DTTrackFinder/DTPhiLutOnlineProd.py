import FWCore.ParameterSet.Config as cms

def DTPhiLutOnlineProd(**kwargs):
  mod = cms.ESProducer('DTPhiLutOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
