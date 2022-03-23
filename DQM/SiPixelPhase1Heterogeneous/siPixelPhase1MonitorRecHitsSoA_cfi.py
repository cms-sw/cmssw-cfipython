import FWCore.ParameterSet.Config as cms

siPixelPhase1MonitorRecHitsSoA = cms.EDProducer('SiPixelPhase1MonitorRecHitsSoA',
  pixelHitsSrc = cms.InputTag('siPixelRecHitsPreSplitting'),
  TopFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsSoA'),
  mightGet = cms.optional.untracked.vstring
)
