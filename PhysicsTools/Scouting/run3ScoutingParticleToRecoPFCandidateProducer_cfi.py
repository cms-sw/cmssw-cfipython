import FWCore.ParameterSet.Config as cms

run3ScoutingParticleToRecoPFCandidateProducer = cms.EDProducer('Run3ScoutingParticleToRecoPFCandidateProducer',
  scoutingparticle = cms.InputTag('hltScoutingPFPacker'),
  softKiller = cms.bool(False),
  CHS = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
