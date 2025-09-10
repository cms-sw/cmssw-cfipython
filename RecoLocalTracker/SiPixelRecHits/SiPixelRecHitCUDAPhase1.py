import FWCore.ParameterSet.Config as cms

def SiPixelRecHitCUDAPhase1(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitCUDAPhase1',
    beamSpot = cms.InputTag('offlineBeamSpotCUDA'),
    src = cms.InputTag('siPixelClustersPreSplittingCUDA'),
    CPE = cms.string('PixelCPEFast'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
