import FWCore.ParameterSet.Config as cms

siPixelTrackComparisonHarvester = cms.EDProducer('SiPixelTrackComparisonHarvester',
  topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/'),
  mightGet = cms.optional.untracked.vstring
)
