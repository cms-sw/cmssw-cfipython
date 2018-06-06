import FWCore.ParameterSet.Config as cms

pfDeepFlavourTagInfos = cms.EDProducer('DeepFlavourTagInfoProducer',
  shallow_tag_infos = cms.InputTag('pfDeepCSVTagInfos'),
  jet_radius = cms.double(0.4),
  min_candidate_pt = cms.double(0.95),
  vertices = cms.InputTag('offlinePrimaryVertices'),
  puppi_value_map = cms.InputTag('puppi'),
  secondary_vertices = cms.InputTag('inclusiveCandidateSecondaryVertices'),
  jets = cms.InputTag('ak4PFJetsCHS'),
  vertex_associator = cms.InputTag('primaryVertexAssociation', 'original'),
  fallback_puppi_weight = cms.bool(False),
  fallback_vertex_association = cms.bool(False)
)
