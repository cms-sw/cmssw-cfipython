import FWCore.ParameterSet.Config as cms

pfHcalGPUComparisonTask = cms.EDProducer('PFHcalGPUComparisonTask',
  name = cms.untracked.string('pfCaloGPUCompDir'),
  pfClusterToken_ref = cms.untracked.InputTag('hltParticleFlowClusterHCALSerialSync'),
  pfClusterToken_target = cms.untracked.InputTag('hltParticleFlowClusterHCAL'),
  mightGet = cms.optional.untracked.vstring
)
