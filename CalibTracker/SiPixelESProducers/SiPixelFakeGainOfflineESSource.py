import FWCore.ParameterSet.Config as cms

def SiPixelFakeGainOfflineESSource(**kwargs):
  mod = cms.ESSource('SiPixelFakeGainOfflineESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
