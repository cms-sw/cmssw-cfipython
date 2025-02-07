import FWCore.ParameterSet.Config as cms

def SiStripDetVOffFakeESSource(*args, **kwargs):
  mod = cms.ESSource('SiStripDetVOffFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
