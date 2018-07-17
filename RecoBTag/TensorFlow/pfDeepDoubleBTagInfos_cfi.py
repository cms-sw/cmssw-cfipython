import FWCore.ParameterSet.Config as cms

pfDeepDoubleBTagInfos = cms.EDProducer('DeepDoubleBTagInfoProducer',
  shallow_tag_infos = cms.InputTag('pfBoostedDoubleSVAK8TagInfos'),
  jet_radius = cms.double(0.8),
  min_candidate_pt = cms.double(0.95),
  vertices = cms.InputTag('offlinePrimaryVertices'),
  secondary_vertices = cms.InputTag('inclusiveCandidateSecondaryVertices'),
  jets = cms.InputTag('ak8PFJetsCHS')
)
