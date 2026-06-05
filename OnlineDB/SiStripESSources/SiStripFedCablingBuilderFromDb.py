import FWCore.ParameterSet.Config as cms

def SiStripFedCablingBuilderFromDb(*args, **kwargs):
  mod = cms.ESSource('SiStripFedCablingBuilderFromDb',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
