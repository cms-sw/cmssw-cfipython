import FWCore.ParameterSet.Config as cms

def SiStripGainBuilderFromDb(**kwargs):
  mod = cms.ESSource('SiStripGainBuilderFromDb',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod