import FWCore.ParameterSet.Config as cms

def PFClusterTimeAssigner(*args, **kwargs):
  mod = cms.EDProducer('PFClusterTimeAssigner',
    src = cms.InputTag('particleFlowClusterECALUncorrected'),
    timeSrc = cms.InputTag('ecalBarrelClusterFastTimer'),
    timeResoSrc = cms.InputTag('ecalBarrelClusterFastTimer'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
