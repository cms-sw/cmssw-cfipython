import FWCore.ParameterSet.Config as cms

siPixelPhase1TrackComparisonHarvester = cms.EDProducer('SiPixelPhase1TrackComparisonHarvester',
  topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/'),
  mightGet = cms.optional.untracked.vstring
)
