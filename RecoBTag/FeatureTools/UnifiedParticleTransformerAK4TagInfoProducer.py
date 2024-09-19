import FWCore.ParameterSet.Config as cms

def UnifiedParticleTransformerAK4TagInfoProducer(**kwargs):
  mod = cms.EDProducer('UnifiedParticleTransformerAK4TagInfoProducer',
    jet_radius = cms.double(0.4),
    min_candidate_pt = cms.double(0.1),
    flip = cms.bool(False),
    sort_cand_by_pt = cms.bool(False),
    fix_lt_sorting = cms.bool(False),
    vertices = cms.InputTag('offlinePrimaryVertices'),
    losttracks = cms.InputTag('lostTracks'),
    puppi_value_map = cms.InputTag('puppi'),
    secondary_vertices = cms.InputTag('inclusiveCandidateSecondaryVertices'),
    jets = cms.InputTag('ak4PFJetsCHS'),
    unsubjet_map = cms.InputTag(''),
    candidates = cms.InputTag('packedPFCandidates'),
    vertex_associator = cms.InputTag('primaryVertexAssociation', 'original'),
    fallback_puppi_weight = cms.bool(False),
    fallback_vertex_association = cms.bool(False),
    is_weighted_jet = cms.bool(False),
    min_jet_pt = cms.double(0),
    max_jet_eta = cms.double(2.5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
