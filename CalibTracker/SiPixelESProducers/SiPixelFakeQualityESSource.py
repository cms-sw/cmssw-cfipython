import FWCore.ParameterSet.Config as cms

def SiPixelFakeQualityESSource(**kwargs):
  mod = cms.ESSource('SiPixelFakeQualityESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
