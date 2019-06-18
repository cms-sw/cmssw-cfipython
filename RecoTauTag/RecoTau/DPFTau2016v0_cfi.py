import FWCore.ParameterSet.Config as cms

DPFTau2016v0 = cms.EDProducer('DPFIsolation',
  pfcands = cms.InputTag('packedPFCandidates'),
  taus = cms.InputTag('slimmedTaus'),
  vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
  graph_file = cms.string('RecoTauTag/TrainingFiles/data/DPFTauId/DPFIsolation_2017v0_quantized.pb'),
  version = cms.uint32(0),
  mem_mapped = cms.bool(False),
  VSallWP = cms.PSet(
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
