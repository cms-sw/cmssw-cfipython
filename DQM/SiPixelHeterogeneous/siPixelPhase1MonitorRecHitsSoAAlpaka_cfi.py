import FWCore.ParameterSet.Config as cms

siPixelPhase1MonitorRecHitsSoAAlpaka = cms.EDProducer('SiPixelPhase1MonitorRecHitsSoAAlpaka',
  pixelHitsSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
  TopFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsAlpaka'),
  mightGet = cms.optional.untracked.vstring
)
