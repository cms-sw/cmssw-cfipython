import FWCore.ParameterSet.Config as cms

def SiStripBadModuleConfigurableFakeESSource(*args, **kwargs):
  mod = cms.ESSource('SiStripBadModuleConfigurableFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
