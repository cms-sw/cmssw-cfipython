import FWCore.ParameterSet.Config as cms

def SiStripApvGainFakeESSource(*args, **kwargs):
  mod = cms.ESSource('SiStripApvGainFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
