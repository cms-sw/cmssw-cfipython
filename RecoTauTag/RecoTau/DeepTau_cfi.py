import FWCore.ParameterSet.Config as cms

DeepTau = cms.EDProducer('DeepTauId',
  electrons = cms.InputTag('slimmedElectrons'),
  muons = cms.InputTag('slimmedMuons'),
  taus = cms.InputTag('slimmedTaus'),
  pfcands = cms.InputTag('packedPFCandidates'),
  vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
  rho = cms.InputTag('fixedGridRhoAll'),
  graph_file = cms.vstring('RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6.pb'),
  mem_mapped = cms.bool(False),
  version = cms.uint32(2),
  debug_level = cms.int32(0),
  disable_dxy_pca = cms.bool(False),
  is_online = cms.bool(False),
  VSeWP = cms.required.vstring,
  VSmuWP = cms.required.vstring,
  VSjetWP = cms.required.vstring,
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
  mightGet = cms.optional.untracked.vstring
)
