import FWCore.ParameterSet.Config as cms

def SiPixelRecHitCUDAHIonPhase1(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitCUDAHIonPhase1',
    beamSpot = cms.InputTag('offlineBeamSpotCUDA'),
    src = cms.InputTag('siPixelClustersPreSplittingCUDA'),
    CPE = cms.string('PixelCPEFastHIonPhase1'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
