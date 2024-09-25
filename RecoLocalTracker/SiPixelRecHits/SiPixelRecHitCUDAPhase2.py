import FWCore.ParameterSet.Config as cms

def SiPixelRecHitCUDAPhase2(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitCUDAPhase2',
    beamSpot = cms.InputTag('offlineBeamSpotCUDA'),
    src = cms.InputTag('siPixelClustersPreSplittingCUDA'),
    CPE = cms.string('PixelCPEFastPhase2'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
