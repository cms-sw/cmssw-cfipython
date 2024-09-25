import FWCore.ParameterSet.Config as cms

def SiStripPedestalsBuilderFromDb(*args, **kwargs):
  mod = cms.ESSource('SiStripPedestalsBuilderFromDb',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
