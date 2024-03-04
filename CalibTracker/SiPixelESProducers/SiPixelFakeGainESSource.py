import FWCore.ParameterSet.Config as cms

def SiPixelFakeGainESSource(**kwargs):
  mod = cms.ESSource('SiPixelFakeGainESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
