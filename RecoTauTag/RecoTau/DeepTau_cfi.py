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
  VSeWP = cms.required.vstring,
  VSmuWP = cms.required.vstring,
  VSjetWP = cms.required.vstring,
  mightGet = cms.optional.untracked.vstring
)
