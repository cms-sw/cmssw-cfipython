import FWCore.ParameterSet.Config as cms

def DTEtaPatternLutOnlineProd(**kwargs):
  mod = cms.ESProducer('DTEtaPatternLutOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
