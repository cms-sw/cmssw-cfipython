import FWCore.ParameterSet.Config as cms

def PackedCandidateGenAssociationProducer(*args, **kwargs):
  mod = cms.EDProducer('PackedCandidateGenAssociationProducer',
    genToPrunedAssoc = cms.InputTag('prunedGenParticles'),
    genToPrunedAssocWithStatusOne = cms.InputTag('prunedGenParticlesWithStatusOne'),
    trackToPackedCandidatesAssoc = cms.InputTag('packedPFCandidates'),
    trackToGenAssoc = cms.required.InputTag,
    tracks = cms.InputTag('generalTracks'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
