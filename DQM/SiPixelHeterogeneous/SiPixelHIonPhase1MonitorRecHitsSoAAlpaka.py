import FWCore.ParameterSet.Config as cms

def SiPixelHIonPhase1MonitorRecHitsSoAAlpaka(*args, **kwargs):
  mod = cms.EDProducer('SiPixelHIonPhase1MonitorRecHitsSoAAlpaka',
    pixelHitsSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
    TopFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsAlpaka'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
