import FWCore.ParameterSet.Config as cms

def SiPixelRecHitCUDAHIonPhase1(**kwargs):
  mod = cms.EDProducer('SiPixelRecHitCUDAHIonPhase1',
    beamSpot = cms.InputTag('offlineBeamSpotCUDA'),
    src = cms.InputTag('siPixelClustersPreSplittingCUDA'),
    CPE = cms.string('PixelCPEFastHIonPhase1'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
