import FWCore.ParameterSet.Config as cms

hltL3MuonSumCaloPFIsolationProducer = cms.EDProducer('L3MuonSumCaloPFIsolationProducer',
  recoChargedCandidateProducer = cms.InputTag('hltL1SeededRecoChargedCandidatePF'),
  pfEcalClusterProducer = cms.InputTag('hltParticleFlowClusterECAL'),
  pfHcalClusterProducer = cms.InputTag('hltParticleFlowClusterHCAL')
)
