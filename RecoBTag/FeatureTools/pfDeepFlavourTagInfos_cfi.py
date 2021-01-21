import FWCore.ParameterSet.Config as cms

pfDeepFlavourTagInfos = cms.EDProducer('DeepFlavourTagInfoProducer',
  shallow_tag_infos = cms.InputTag('pfDeepCSVTagInfos'),
  jet_radius = cms.double(0.4),
  min_candidate_pt = cms.double(0.95),
  flip = cms.bool(False),
  vertices = cms.InputTag('offlinePrimaryVertices'),
  puppi_value_map = cms.InputTag('puppi'),
  secondary_vertices = cms.InputTag('inclusiveCandidateSecondaryVertices'),
  jets = cms.InputTag('ak4PFJetsCHS'),
  candidates = cms.InputTag('packedPFCandidates'),
  vertex_associator = cms.InputTag('primaryVertexAssociation', 'original'),
  fallback_puppi_weight = cms.bool(False),
  fallback_vertex_association = cms.bool(False),
  run_deepVertex = cms.bool(False),
  compute_probabilities = cms.bool(False),
  min_jet_pt = cms.double(15),
  max_jet_eta = cms.double(2.5)
)
