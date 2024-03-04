import FWCore.ParameterSet.Config as cms

def SiStripQualityFakeESSource(**kwargs):
  mod = cms.ESSource('SiStripQualityFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
