import FWCore.ParameterSet.Config as cms

def SiStripBadFiberFakeESSource(*args, **kwargs):
  mod = cms.ESSource('SiStripBadFiberFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
