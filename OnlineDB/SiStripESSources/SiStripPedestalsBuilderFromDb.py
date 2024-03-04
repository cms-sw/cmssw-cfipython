import FWCore.ParameterSet.Config as cms

def SiStripPedestalsBuilderFromDb(**kwargs):
  mod = cms.ESSource('SiStripPedestalsBuilderFromDb',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
