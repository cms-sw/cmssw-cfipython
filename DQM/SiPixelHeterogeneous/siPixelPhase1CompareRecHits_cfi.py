import FWCore.ParameterSet.Config as cms

siPixelPhase1CompareRecHits = cms.EDProducer('SiPixelPhase1CompareRecHits',
  pixelHitsReferenceSoA = cms.InputTag('siPixelRecHitsPreSplittingAlpakaSerial'),
  pixelHitsTargetSoA = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsCompareDeviceVSHost'),
  minD2cut = cms.double(0.0001),
  mightGet = cms.optional.untracked.vstring
)
