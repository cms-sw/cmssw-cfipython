import FWCore.ParameterSet.Config as cms

def SiPixelPhase2CompareRecHits(*args, **kwargs):
  mod = cms.EDProducer('SiPixelPhase2CompareRecHits',
    pixelHitsReferenceSoA = cms.InputTag('siPixelRecHitsPreSplittingAlpakaSerial'),
    pixelHitsTargetSoA = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsCompareDeviceVSHost'),
    minD2cut = cms.double(0.0001),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
