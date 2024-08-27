import FWCore.ParameterSet.Config as cms

def SiPixelPhase1MonitorRecHitsSoAAlpaka(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1MonitorRecHitsSoAAlpaka',
    pixelHitsSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
    TopFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsAlpaka'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
