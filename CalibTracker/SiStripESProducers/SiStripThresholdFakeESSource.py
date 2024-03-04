import FWCore.ParameterSet.Config as cms

def SiStripThresholdFakeESSource(**kwargs):
  mod = cms.ESSource('SiStripThresholdFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
