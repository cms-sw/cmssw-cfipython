import FWCore.ParameterSet.Config as cms

def DeepDoubleXTagInfoProducer(**kwargs):
  mod = cms.EDProducer('DeepDoubleXTagInfoProducer',
    shallow_tag_infos = cms.InputTag('pfBoostedDoubleSVAK8TagInfos'),
    jet_radius = cms.double(0.8),
    min_jet_pt = cms.double(150),
    min_candidate_pt = cms.double(0.95),
    vertices = cms.InputTag('offlinePrimaryVertices'),
    puppi_value_map = cms.InputTag('puppi'),
    secondary_vertices = cms.InputTag('inclusiveCandidateSecondaryVertices'),
    jets = cms.InputTag('ak8PFJetsPuppi'),
    fallback_puppi_weight = cms.bool(False),
    is_weighted_jet = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
