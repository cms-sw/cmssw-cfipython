import FWCore.ParameterSet.Config as cms

def SiPixelRecHitCUDAPhase1(**kwargs):
  mod = cms.EDProducer('SiPixelRecHitCUDAPhase1',
    beamSpot = cms.InputTag('offlineBeamSpotCUDA'),
    src = cms.InputTag('siPixelClustersPreSplittingCUDA'),
    CPE = cms.string('PixelCPEFast'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
