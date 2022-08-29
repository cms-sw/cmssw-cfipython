import FWCore.ParameterSet.Config as cms

siPixelPhase1MonitorRecHitsSoA = cms.EDProducer('SiPixelPhase1MonitorRecHitsSoA',
  pixelHitsSrc = cms.InputTag('siPixelRecHitsPreSplittingSoA'),
  TopFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsSoA'),
  mightGet = cms.optional.untracked.vstring
)
