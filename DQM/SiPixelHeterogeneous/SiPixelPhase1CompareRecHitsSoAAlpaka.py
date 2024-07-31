import FWCore.ParameterSet.Config as cms

def SiPixelPhase1CompareRecHitsSoAAlpaka(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1CompareRecHitsSoAAlpaka',
    pixelHitsSrcHost = cms.InputTag('siPixelRecHitsPreSplittingAlpakaSerial'),
    pixelHitsSrcDevice = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsCompareDeviceVSHost'),
    minD2cut = cms.double(0.0001),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
