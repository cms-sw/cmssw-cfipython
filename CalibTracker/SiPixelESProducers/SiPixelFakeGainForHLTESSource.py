import FWCore.ParameterSet.Config as cms

def SiPixelFakeGainForHLTESSource(*args, **kwargs):
  mod = cms.ESSource('SiPixelFakeGainForHLTESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
