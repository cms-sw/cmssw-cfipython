import FWCore.ParameterSet.Config as cms

def SiStripFedCablingFakeESSource(*args, **kwargs):
  mod = cms.ESSource('SiStripFedCablingFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
