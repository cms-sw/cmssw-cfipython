import FWCore.ParameterSet.Config as cms

packedCandidatesGenAssociationDefault = cms.EDProducer('PackedCandidateGenAssociationProducer',
  genToPrunedAssoc = cms.InputTag('prunedGenParticles'),
  genToPrunedAssocWithStatusOne = cms.InputTag('prunedGenParticlesWithStatusOne'),
  trackToPackedCandidatesAssoc = cms.InputTag('packedPFCandidates'),
  trackToGenAssoc = cms.required.InputTag,
  tracks = cms.InputTag('generalTracks'),
  mightGet = cms.optional.untracked.vstring
)
