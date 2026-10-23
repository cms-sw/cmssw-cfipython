import FWCore.ParameterSet.Config as cms

def SiStripBadStripFakeESSource(*args, **kwargs):
  mod = cms.ESSource('SiStripBadStripFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
