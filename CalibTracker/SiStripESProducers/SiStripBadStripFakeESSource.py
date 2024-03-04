import FWCore.ParameterSet.Config as cms

def SiStripBadStripFakeESSource(**kwargs):
  mod = cms.ESSource('SiStripBadStripFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
