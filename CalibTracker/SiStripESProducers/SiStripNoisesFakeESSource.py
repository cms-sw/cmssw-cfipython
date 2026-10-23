import FWCore.ParameterSet.Config as cms

def SiStripNoisesFakeESSource(*args, **kwargs):
  mod = cms.ESSource('SiStripNoisesFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
