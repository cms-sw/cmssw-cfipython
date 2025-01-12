import FWCore.ParameterSet.Config as cms

def SeedClusterRemoverPhase2(*args, **kwargs):
  mod = cms.EDProducer('SeedClusterRemoverPhase2',
    doOuterTracker = cms.bool(True),
    doPixel = cms.bool(True),
    trajectories = cms.InputTag('initialStepSeeds'),
    pixelClusters = cms.InputTag('siPixelClusters'),
    phase2OTClusters = cms.InputTag('siPhase2Clusters'),
    oldClusterRemovalInfo = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
