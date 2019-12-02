import FWCore.ParameterSet.Config as cms

pfDeepDoubleXTagInfos = cms.EDProducer('DeepDoubleXTagInfoProducer',
  shallow_tag_infos = cms.InputTag('pfBoostedDoubleSVAK8TagInfos'),
  jet_radius = cms.double(0.8),
  min_jet_pt = cms.double(150),
  min_candidate_pt = cms.double(0.95),
  vertices = cms.InputTag('offlinePrimaryVertices'),
  secondary_vertices = cms.InputTag('inclusiveCandidateSecondaryVertices'),
  jets = cms.InputTag('ak8PFJetsCHS'),
  mightGet = cms.optional.untracked.vstring
)
