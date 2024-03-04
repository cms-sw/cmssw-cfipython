import FWCore.ParameterSet.Config as cms

def SiPixelFakeGainForHLTESSource(**kwargs):
  mod = cms.ESSource('SiPixelFakeGainForHLTESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
