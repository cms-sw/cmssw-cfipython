import FWCore.ParameterSet.Config as cms

def SiStripPedestalsFakeESSource(*args, **kwargs):
  mod = cms.ESSource('SiStripPedestalsFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
