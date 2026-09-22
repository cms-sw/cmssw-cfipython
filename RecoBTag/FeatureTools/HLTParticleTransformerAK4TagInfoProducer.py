import FWCore.ParameterSet.Config as cms

def HLTParticleTransformerAK4TagInfoProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTParticleTransformerAK4TagInfoProducer',
    jet_radius = cms.double(0.4),
    min_candidate_pt = cms.double(0.95),
    vertices = cms.InputTag('hltOfflinePrimaryVertices'),
    secondary_vertices = cms.InputTag('hltInclusiveCandidateSecondaryVertices'),
    jets = cms.InputTag('hltAK4PFPuppiJets'),
    candidates = cms.InputTag('hltParticleFlowTmp'),
    min_jet_pt = cms.double(15),
    max_jet_eta = cms.double(2.5),
    fallback_vertex_association = cms.bool(False),
    vertex_associator = cms.InputTag('hltPrimaryVertexAssociation', 'original'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
