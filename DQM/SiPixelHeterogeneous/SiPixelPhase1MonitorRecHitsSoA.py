import FWCore.ParameterSet.Config as cms

def SiPixelPhase1MonitorRecHitsSoA(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1MonitorRecHitsSoA',
    pixelHitsSrc = cms.InputTag('siPixelRecHitsPreSplittingSoA'),
    TopFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsSoA'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
