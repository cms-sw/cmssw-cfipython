import FWCore.ParameterSet.Config as cms

def SiStripBadModuleConfigurableFakeESSource(**kwargs):
  mod = cms.ESSource('SiStripBadModuleConfigurableFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
