import FWCore.ParameterSet.Config as cms

def SiPixelPhase1MonitorRecHitsSoA(*args, **kwargs):
  mod = cms.EDProducer('SiPixelPhase1MonitorRecHitsSoA',
    pixelHitsSrc = cms.InputTag('siPixelRecHitsPreSplittingSoA'),
    TopFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsSoA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
