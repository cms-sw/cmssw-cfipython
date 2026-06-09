import FWCore.ParameterSet.Config as cms

def Run3ScoutingParticleToPackedCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('Run3ScoutingParticleToPackedCandidateProducer',
    src = cms.InputTag('hltScoutingPFPacker'),
    vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
    tracks = cms.InputTag('scoutingTracks'),
    CHS = cms.bool(False),
    covarianceVersion = cms.int32(1),
    covarianceSchema = cms.int32(520),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
