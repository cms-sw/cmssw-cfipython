import FWCore.ParameterSet.Config as cms

def SiPixelFakeGainESSource(*args, **kwargs):
  mod = cms.ESSource('SiPixelFakeGainESSource',
    file = cms.FileInPath('CalibTracker/SiPixelESProducers/data/PixelSkimmedGeometry.txt'),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
