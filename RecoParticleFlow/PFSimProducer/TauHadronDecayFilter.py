import FWCore.ParameterSet.Config as cms

def TauHadronDecayFilter(*args, **kwargs):
  mod = cms.EDFilter('TauHadronDecayFilter',
    particles = cms.InputTag('particleFlowBlock'),
    ParticleFilter = cms.PSet(
      etaMax = cms.double(10),
      pTMin = cms.double(0),
      EMin = cms.double(0)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
