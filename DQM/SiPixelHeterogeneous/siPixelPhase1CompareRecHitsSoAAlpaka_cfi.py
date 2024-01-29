import FWCore.ParameterSet.Config as cms

siPixelPhase1CompareRecHitsSoAAlpaka = cms.EDProducer('SiPixelPhase1CompareRecHitsSoAAlpaka',
  pixelHitsSrcHost = cms.InputTag('siPixelRecHitsPreSplittingAlpakaSerial'),
  pixelHitsSrcDevice = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsCompareDeviceVSHost'),
  minD2cut = cms.double(0.0001),
  mightGet = cms.optional.untracked.vstring
)
