import FWCore.ParameterSet.Config as cms

def SiPixelFakeQualityESSource(*args, **kwargs):
  mod = cms.ESSource('SiPixelFakeQualityESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
