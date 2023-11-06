import FWCore.ParameterSet.Config as cms

particleFlowClusterTimeAssignerDefault = cms.EDProducer('PFClusterTimeAssigner',
  src = cms.InputTag('particleFlowClusterECALUncorrected'),
  timeSrc = cms.InputTag('ecalBarrelClusterFastTimer'),
  timeResoSrc = cms.InputTag('ecalBarrelClusterFastTimer'),
  mightGet = cms.optional.untracked.vstring
)
