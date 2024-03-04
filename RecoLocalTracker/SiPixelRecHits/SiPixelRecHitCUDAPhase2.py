import FWCore.ParameterSet.Config as cms

def SiPixelRecHitCUDAPhase2(**kwargs):
  mod = cms.EDProducer('SiPixelRecHitCUDAPhase2',
    beamSpot = cms.InputTag('offlineBeamSpotCUDA'),
    src = cms.InputTag('siPixelClustersPreSplittingCUDA'),
    CPE = cms.string('PixelCPEFastPhase2'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
