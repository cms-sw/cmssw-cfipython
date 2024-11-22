import FWCore.ParameterSet.Config as cms

def Phase2TrackerCablingCfgESSource(*args, **kwargs):
  mod = cms.ESSource('Phase2TrackerCablingCfgESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
