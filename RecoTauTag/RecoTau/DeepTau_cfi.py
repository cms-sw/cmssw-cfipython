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
  VSeWP = cms.PSet(
    VVVLoose = cms.string('0'),
    VVLoose = cms.string('0'),
    VLoose = cms.string('0'),
    Loose = cms.string('0'),
    Medium = cms.string('0'),
    Tight = cms.string('0'),
    VTight = cms.string('0'),
    VVTight = cms.string('0'),
    VVVTight = cms.string('0')
  ),
  VSmuWP = cms.PSet(
    VVVLoose = cms.string('0'),
    VVLoose = cms.string('0'),
    VLoose = cms.string('0'),
    Loose = cms.string('0'),
    Medium = cms.string('0'),
    Tight = cms.string('0'),
    VTight = cms.string('0'),
    VVTight = cms.string('0'),
    VVVTight = cms.string('0')
  ),
  VSjetWP = cms.PSet(
    VVVLoose = cms.string('0'),
    VVLoose = cms.string('0'),
    VLoose = cms.string('0'),
    Loose = cms.string('0'),
    Medium = cms.string('0'),
    Tight = cms.string('0'),
    VTight = cms.string('0'),
    VVTight = cms.string('0'),
    VVVTight = cms.string('0')
  ),
  mightGet = cms.optional.untracked.vstring
)
