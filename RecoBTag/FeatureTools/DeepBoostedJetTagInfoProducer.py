import FWCore.ParameterSet.Config as cms

def DeepBoostedJetTagInfoProducer(**kwargs):
  mod = cms.EDProducer('DeepBoostedJetTagInfoProducer',
    jet_radius = cms.double(0.8),
    min_jet_pt = cms.double(150),
    max_jet_eta = cms.double(99),
    min_pt_for_track_properties = cms.double(-1),
    min_pt_for_pfcandidates = cms.double(-1),
    use_puppiP4 = cms.bool(True),
    include_neutrals = cms.bool(True),
    sort_by_sip2dsig = cms.bool(False),
    min_puppi_wgt = cms.double(0.01),
    flip_ip_sign = cms.bool(False),
    sip3dSigMax = cms.double(-1),
    use_hlt_features = cms.bool(False),
    vertices = cms.InputTag('offlinePrimaryVertices'),
    secondary_vertices = cms.InputTag('inclusiveCandidateSecondaryVertices'),
    pf_candidates = cms.InputTag('particleFlow'),
    jets = cms.InputTag('ak8PFJetsPuppi'),
    unsubjet_map = cms.untracked.InputTag(''),
    puppi_value_map = cms.InputTag('puppi'),
    vertex_associator = cms.InputTag('primaryVertexAssociation', 'original'),
    use_scouting_features = cms.bool(False),
    normchi2_value_map = cms.InputTag(''),
    dz_value_map = cms.InputTag(''),
    dxy_value_map = cms.InputTag(''),
    dzsig_value_map = cms.InputTag(''),
    dxysig_value_map = cms.InputTag(''),
    lostInnerHits_value_map = cms.InputTag(''),
    quality_value_map = cms.InputTag(''),
    trkPt_value_map = cms.InputTag(''),
    trkEta_value_map = cms.InputTag(''),
    trkPhi_value_map = cms.InputTag(''),
    covarianceVersion = cms.int32(0),
    covariancePackingSchemas = cms.vint32(
      8,
      264,
      520,
      776,
      0
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
