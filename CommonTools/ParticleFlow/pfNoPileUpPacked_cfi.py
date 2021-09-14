import FWCore.ParameterSet.Config as cms

pfNoPileUpPacked = cms.EDProducer('PFNoPileUpPacked',
  candidates = cms.InputTag('packedPFCandidates'),
  vertexAssociationQuality = cms.int32(7),
  vertexAssociation = cms.InputTag('packedPrimaryVertexAssociationJME', 'original'),
  mightGet = cms.optional.untracked.vstring
)
