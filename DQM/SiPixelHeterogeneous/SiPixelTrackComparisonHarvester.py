import FWCore.ParameterSet.Config as cms

def SiPixelTrackComparisonHarvester(*args, **kwargs):
  mod = cms.EDProducer('SiPixelTrackComparisonHarvester',
    topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
