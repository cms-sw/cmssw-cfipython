import FWCore.ParameterSet.Config as cms

def SiStripDetVOffFakeESSource(**kwargs):
  mod = cms.ESSource('SiStripDetVOffFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
