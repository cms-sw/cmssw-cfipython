import FWCore.ParameterSet.Config as cms

pfDeepBoostedJetTagInfos = cms.EDProducer('DeepBoostedJetTagInfoProducer',
  has_puppi_weighted_daughters = cms.bool(True),
  jet_radius = cms.double(0.8),
  min_jet_pt = cms.double(150),
  min_pt_for_track_properties = cms.double(-1),
  vertices = cms.InputTag('offlinePrimaryVertices'),
  secondary_vertices = cms.InputTag('inclusiveCandidateSecondaryVertices'),
  jets = cms.InputTag('ak8PFJetsPuppi'),
  puppi_value_map = cms.InputTag('puppi'),
  vertex_associator = cms.InputTag('primaryVertexAssociation', 'original'),
  mightGet = cms.optional.untracked.vstring
)
