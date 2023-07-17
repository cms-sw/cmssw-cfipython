import FWCore.ParameterSet.Config as cms

siPixelHIonPhase1MonitorRecHitsSoA = cms.EDProducer('SiPixelHIonPhase1MonitorRecHitsSoA',
  pixelHitsSrc = cms.InputTag('siPixelRecHitsPreSplittingSoA'),
  TopFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsSoA'),
  mightGet = cms.optional.untracked.vstring
)
