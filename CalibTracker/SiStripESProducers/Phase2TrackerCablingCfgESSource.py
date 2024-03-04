import FWCore.ParameterSet.Config as cms

def Phase2TrackerCablingCfgESSource(**kwargs):
  mod = cms.ESSource('Phase2TrackerCablingCfgESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
