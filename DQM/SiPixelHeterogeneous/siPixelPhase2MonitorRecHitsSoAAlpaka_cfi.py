import FWCore.ParameterSet.Config as cms

siPixelPhase2MonitorRecHitsSoAAlpaka = cms.EDProducer('SiPixelPhase2MonitorRecHitsSoAAlpaka',
  pixelHitsSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
  TopFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsAlpaka'),
  mightGet = cms.optional.untracked.vstring
)
