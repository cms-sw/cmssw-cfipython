import FWCore.ParameterSet.Config as cms

def DTExtLutOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('DTExtLutOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
