import FWCore.ParameterSet.Config as cms

def SiStripThresholdFakeESSource(*args, **kwargs):
  mod = cms.ESSource('SiStripThresholdFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
