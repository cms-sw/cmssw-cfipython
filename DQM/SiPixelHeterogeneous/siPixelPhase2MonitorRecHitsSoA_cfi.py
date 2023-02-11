import FWCore.ParameterSet.Config as cms

siPixelPhase2MonitorRecHitsSoA = cms.EDProducer('SiPixelPhase2MonitorRecHitsSoA',
  pixelHitsSrc = cms.InputTag('siPixelRecHitsPreSplittingSoA'),
  TopFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsSoA'),
  mightGet = cms.optional.untracked.vstring
)
