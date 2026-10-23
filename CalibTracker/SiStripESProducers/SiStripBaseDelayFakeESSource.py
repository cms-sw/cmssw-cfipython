import FWCore.ParameterSet.Config as cms

def SiStripBaseDelayFakeESSource(*args, **kwargs):
  mod = cms.ESSource('SiStripBaseDelayFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
