import FWCore.ParameterSet.Config as cms

def SiStripFedCablingBuilderFromDb(**kwargs):
  mod = cms.ESSource('SiStripFedCablingBuilderFromDb',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
