import FWCore.ParameterSet.Config as cms

packedCandidatesGenAssociationDefault = cms.EDProducer('PackedCandidateGenAssociationProducer',
  genToPrunedAssoc = cms.InputTag('prunedGenParticles'),
  genToPrunedAssocWithStatusOne = cms.InputTag('prunedGenParticlesWithStatusOne'),
  trackToPackedCandidatesAssoc = cms.InputTag('packedPFCandidates'),
  tracks = cms.InputTag('generalTracks')
)
