import FWCore.ParameterSet.Config as cms

def SiPixelHIonPhase1CompareRecHits(**kwargs):
  mod = cms.EDProducer('SiPixelHIonPhase1CompareRecHits',
    pixelHitsReferenceSoA = cms.InputTag('siPixelRecHitsPreSplittingAlpakaSerial'),
    pixelHitsTargetSoA = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsCompareDeviceVSHost'),
    minD2cut = cms.double(0.0001),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod