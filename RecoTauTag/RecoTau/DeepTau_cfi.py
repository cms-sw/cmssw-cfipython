import FWCore.ParameterSet.Config as cms

DeepTau = cms.EDProducer('DeepTauId',
  electrons = cms.InputTag('slimmedElectrons'),
  muons = cms.InputTag('slimmedMuons'),
  taus = cms.InputTag('slimmedTaus'),
  pfcands = cms.InputTag('packedPFCandidates'),
  vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
  rho = cms.InputTag('fixedGridRhoAll'),
  mem_mapped = cms.bool(False),
  year = cms.uint32(2017),
  version = cms.uint32(2),
  sub_version = cms.uint32(1),
  debug_level = cms.int32(0),
  disable_dxy_pca = cms.bool(False),
  disable_hcalFraction_workaround = cms.bool(False),
  disable_CellIndex_workaround = cms.bool(False),
  save_inputs = cms.bool(False),
  is_online = cms.bool(False),
  VSeWP = cms.vstring('-1.'),
  VSmuWP = cms.vstring('-1.'),
  VSjetWP = cms.vstring('-1.'),
  basicTauDiscriminators = cms.untracked.InputTag('basicTauDiscriminators'),
  basicTauDiscriminatorsdR03 = cms.untracked.InputTag('basicTauDiscriminatorsdR03'),
  pfTauTransverseImpactParameters = cms.InputTag('hpsPFTauTransverseImpactParameters'),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    decayMode = cms.PSet(
      cut = cms.required.double,
      Producer = cms.required.InputTag
    )
  ),
  graph_file = cms.vstring('RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6.pb'),
  mightGet = cms.optional.untracked.vstring
)
