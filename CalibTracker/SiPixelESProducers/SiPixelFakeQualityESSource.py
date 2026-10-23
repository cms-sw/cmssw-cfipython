import FWCore.ParameterSet.Config as cms

def SiPixelFakeQualityESSource(*args, **kwargs):
  mod = cms.ESSource('SiPixelFakeQualityESSource',
    file = cms.FileInPath('CalibTracker/SiPixelESProducers/data/PixelSkimmedGeometry.txt'),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
