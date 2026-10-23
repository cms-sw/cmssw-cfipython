import FWCore.ParameterSet.Config as cms

def L3MuonSumCaloPFIsolationProducer(*args, **kwargs):
  mod = cms.EDProducer('L3MuonSumCaloPFIsolationProducer',
    recoChargedCandidateProducer = cms.InputTag('hltL1SeededRecoChargedCandidatePF'),
    pfEcalClusterProducer = cms.InputTag('hltParticleFlowClusterECAL'),
    pfHcalClusterProducer = cms.InputTag('hltParticleFlowClusterHCAL'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
