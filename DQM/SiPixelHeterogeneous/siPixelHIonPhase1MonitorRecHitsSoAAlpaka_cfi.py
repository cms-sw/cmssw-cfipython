import FWCore.ParameterSet.Config as cms

siPixelHIonPhase1MonitorRecHitsSoAAlpaka = cms.EDProducer('SiPixelHIonPhase1MonitorRecHitsSoAAlpaka',
  pixelHitsSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
  TopFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsAlpaka'),
  mightGet = cms.optional.untracked.vstring
)
