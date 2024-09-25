import FWCore.ParameterSet.Config as cms

def Run3ScoutingParticleToRecoPFCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('Run3ScoutingParticleToRecoPFCandidateProducer',
    scoutingparticle = cms.InputTag('hltScoutingPFPacker'),
    softKiller = cms.bool(False),
    CHS = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
