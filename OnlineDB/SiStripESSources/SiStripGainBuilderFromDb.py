import FWCore.ParameterSet.Config as cms

def SiStripGainBuilderFromDb(*args, **kwargs):
  mod = cms.ESSource('SiStripGainBuilderFromDb',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
