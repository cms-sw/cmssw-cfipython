import FWCore.ParameterSet.Config as cms

def L3MuonSumCaloPFIsolationProducer(**kwargs):
  mod = cms.EDProducer('L3MuonSumCaloPFIsolationProducer',
    recoChargedCandidateProducer = cms.InputTag('hltL1SeededRecoChargedCandidatePF'),
    pfEcalClusterProducer = cms.InputTag('hltParticleFlowClusterECAL'),
    pfHcalClusterProducer = cms.InputTag('hltParticleFlowClusterHCAL'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
