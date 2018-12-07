import FWCore.ParameterSet.Config as cms

DeepTau2017v1 = cms.EDProducer('DeepTauId',
  electrons = cms.InputTag('slimmedElectrons'),
  muons = cms.InputTag('slimmedMuons'),
  taus = cms.InputTag('slimmedTaus'),
  graph_file = cms.string('RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v1_20L1024N_quantized.pb'),
  mem_mapped = cms.bool(False),
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
  )
)
