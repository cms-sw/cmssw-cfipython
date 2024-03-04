import FWCore.ParameterSet.Config as cms

def SiStripBadFiberFakeESSource(**kwargs):
  mod = cms.ESSource('SiStripBadFiberFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
