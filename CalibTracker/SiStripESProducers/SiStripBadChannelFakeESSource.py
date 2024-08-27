import FWCore.ParameterSet.Config as cms

def SiStripBadChannelFakeESSource(**kwargs):
  mod = cms.ESSource('SiStripBadChannelFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
