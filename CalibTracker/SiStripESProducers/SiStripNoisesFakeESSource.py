import FWCore.ParameterSet.Config as cms

def SiStripNoisesFakeESSource(**kwargs):
  mod = cms.ESSource('SiStripNoisesFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
