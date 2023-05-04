import FWCore.ParameterSet.Config as cms

siPixelPhase2CompareRecHitsSoA = cms.EDProducer('SiPixelPhase2CompareRecHitsSoA',
  pixelHitsSrcCPU = cms.InputTag('siPixelRecHitsPreSplittingSoA@Host'),
  pixelHitsSrcGPU = cms.InputTag('siPixelRecHitsPreSplittingSoA@cuda'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsCompareDevicevsHost'),
  minD2cut = cms.double(0.0001),
  mightGet = cms.optional.untracked.vstring
)
