import FWCore.ParameterSet.Config as cms

def SiStripNoiseBuilderFromDb(*args, **kwargs):
  mod = cms.ESSource('SiStripNoiseBuilderFromDb',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
