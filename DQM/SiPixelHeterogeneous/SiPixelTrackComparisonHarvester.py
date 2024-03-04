import FWCore.ParameterSet.Config as cms

def SiPixelTrackComparisonHarvester(**kwargs):
  mod = cms.EDProducer('SiPixelTrackComparisonHarvester',
    topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
