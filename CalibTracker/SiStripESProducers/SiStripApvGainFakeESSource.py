import FWCore.ParameterSet.Config as cms

def SiStripApvGainFakeESSource(**kwargs):
  mod = cms.ESSource('SiStripApvGainFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
