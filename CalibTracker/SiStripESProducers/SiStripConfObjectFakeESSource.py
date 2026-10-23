import FWCore.ParameterSet.Config as cms

def SiStripConfObjectFakeESSource(*args, **kwargs):
  mod = cms.ESSource('SiStripConfObjectFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
