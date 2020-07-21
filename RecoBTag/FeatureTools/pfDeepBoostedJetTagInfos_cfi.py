import FWCore.ParameterSet.Config as cms

pfDeepBoostedJetTagInfos = cms.EDProducer('DeepBoostedJetTagInfoProducer',
  jet_radius = cms.double(0.8),
  min_jet_pt = cms.double(150),
  min_pt_for_track_properties = cms.double(-1),
  use_puppiP4 = cms.bool(True),
  include_neutrals = cms.bool(True),
  sort_by_sip2dsig = cms.bool(False),
  min_puppi_wgt = cms.double(0.01),
  vertices = cms.InputTag('offlinePrimaryVertices'),
  secondary_vertices = cms.InputTag('inclusiveCandidateSecondaryVertices'),
  pf_candidates = cms.InputTag('particleFlow'),
  jets = cms.InputTag('ak8PFJetsPuppi'),
  puppi_value_map = cms.InputTag('puppi'),
  vertex_associator = cms.InputTag('primaryVertexAssociation', 'original')
)
