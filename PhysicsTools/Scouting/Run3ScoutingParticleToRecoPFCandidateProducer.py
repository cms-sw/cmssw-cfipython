import FWCore.ParameterSet.Config as cms

def Run3ScoutingParticleToRecoPFCandidateProducer(**kwargs):
  mod = cms.EDProducer('Run3ScoutingParticleToRecoPFCandidateProducer',
    scoutingparticle = cms.InputTag('hltScoutingPFPacker'),
    softKiller = cms.bool(False),
    CHS = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
