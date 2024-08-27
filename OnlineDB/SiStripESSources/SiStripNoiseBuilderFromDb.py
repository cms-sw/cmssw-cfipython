import FWCore.ParameterSet.Config as cms

def SiStripNoiseBuilderFromDb(**kwargs):
  mod = cms.ESSource('SiStripNoiseBuilderFromDb',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
