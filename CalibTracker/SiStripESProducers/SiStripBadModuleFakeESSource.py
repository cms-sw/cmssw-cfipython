import FWCore.ParameterSet.Config as cms

def SiStripBadModuleFakeESSource(**kwargs):
  mod = cms.ESSource('SiStripBadModuleFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod