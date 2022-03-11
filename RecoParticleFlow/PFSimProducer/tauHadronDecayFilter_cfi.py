import FWCore.ParameterSet.Config as cms

tauHadronDecayFilter = cms.EDFilter('TauHadronDecayFilter',
  particles = cms.InputTag('particleFlowBlock'),
  ParticleFilter = cms.PSet(
    etaMax = cms.double(10),
    pTMin = cms.double(0),
    EMin = cms.double(0)
  ),
  mightGet = cms.optional.untracked.vstring
)
