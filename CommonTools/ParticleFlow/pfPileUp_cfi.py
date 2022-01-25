import FWCore.ParameterSet.Config as cms

pfPileUp = cms.EDProducer('PFPileUp',
  PFCandidates = cms.InputTag('particleFlowTmpPtrs'),
  Vertices = cms.InputTag('offlinePrimaryVertices'),
  enable = cms.bool(True),
  verbose = cms.untracked.bool(False),
  checkClosestZVertex = cms.bool(True),
  useVertexAssociation = cms.bool(False),
  vertexAssociationQuality = cms.int32(0),
  vertexAssociation = cms.InputTag(''),
  NumOfPUVtxsForCharged = cms.uint32(0),
  DzCutForChargedFromPUVtxs = cms.double(0.2),
  mightGet = cms.optional.untracked.vstring
)
