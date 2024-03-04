import FWCore.ParameterSet.Config as cms

def DTQualPatternLutOnlineProd(**kwargs):
  mod = cms.ESProducer('DTQualPatternLutOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
