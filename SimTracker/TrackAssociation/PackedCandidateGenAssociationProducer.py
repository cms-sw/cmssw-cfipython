import FWCore.ParameterSet.Config as cms

def PackedCandidateGenAssociationProducer(**kwargs):
  mod = cms.EDProducer('PackedCandidateGenAssociationProducer',
    genToPrunedAssoc = cms.InputTag('prunedGenParticles'),
    genToPrunedAssocWithStatusOne = cms.InputTag('prunedGenParticlesWithStatusOne'),
    trackToPackedCandidatesAssoc = cms.InputTag('packedPFCandidates'),
    trackToGenAssoc = cms.required.InputTag,
    tracks = cms.InputTag('generalTracks'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
