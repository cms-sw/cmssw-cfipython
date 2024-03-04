import FWCore.ParameterSet.Config as cms

def PFClusterTimeAssigner(**kwargs):
  mod = cms.EDProducer('PFClusterTimeAssigner',
    src = cms.InputTag('particleFlowClusterECALUncorrected'),
    timeSrc = cms.InputTag('ecalBarrelClusterFastTimer'),
    timeResoSrc = cms.InputTag('ecalBarrelClusterFastTimer'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
