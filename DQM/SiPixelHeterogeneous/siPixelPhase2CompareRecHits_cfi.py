import FWCore.ParameterSet.Config as cms

siPixelPhase2CompareRecHits = cms.EDProducer('SiPixelPhase2CompareRecHits',
  pixelHitsReferenceSoA = cms.InputTag('siPixelRecHitsPreSplittingAlpakaSerial'),
  pixelHitsTargetSoA = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsCompareDeviceVSHost'),
  minD2cut = cms.double(0.0001),
  mightGet = cms.optional.untracked.vstring
)
