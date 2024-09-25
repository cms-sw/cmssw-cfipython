import FWCore.ParameterSet.Config as cms

def DTQualPatternLutOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('DTQualPatternLutOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
