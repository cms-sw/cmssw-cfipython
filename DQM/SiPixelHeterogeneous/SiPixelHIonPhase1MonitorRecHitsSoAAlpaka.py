import FWCore.ParameterSet.Config as cms

def SiPixelHIonPhase1MonitorRecHitsSoAAlpaka(**kwargs):
  mod = cms.EDProducer('SiPixelHIonPhase1MonitorRecHitsSoAAlpaka',
    pixelHitsSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
    TopFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsAlpaka'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
