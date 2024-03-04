import FWCore.ParameterSet.Config as cms

def SiStripPedestalsFakeESSource(**kwargs):
  mod = cms.ESSource('SiStripPedestalsFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
