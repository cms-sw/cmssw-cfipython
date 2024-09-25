import FWCore.ParameterSet.Config as cms

def SiStripHashedDetIdESModule(*args, **kwargs):
  mod = cms.ESProducer('SiStripHashedDetIdESModule',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
