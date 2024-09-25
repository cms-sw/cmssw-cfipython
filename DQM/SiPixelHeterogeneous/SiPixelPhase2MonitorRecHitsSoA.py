import FWCore.ParameterSet.Config as cms

def SiPixelPhase2MonitorRecHitsSoA(*args, **kwargs):
  mod = cms.EDProducer('SiPixelPhase2MonitorRecHitsSoA',
    pixelHitsSrc = cms.InputTag('siPixelRecHitsPreSplittingSoA'),
    TopFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsSoA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
