import FWCore.ParameterSet.Config as cms

DPFTau2016v0 = cms.EDProducer('DPFIsolation',
  pfcands = cms.InputTag('packedPFCandidates'),
  taus = cms.InputTag('slimmedTaus'),
  vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
  graph_file = cms.vstring('RecoTauTag/TrainingFiles/data/DPFTauId/DPFIsolation_2017v0_quantized.pb'),
  version = cms.uint32(0),
  mem_mapped = cms.bool(False),
  is_online = cms.bool(False),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    decayMode = cms.PSet(
      cut = cms.required.double,
      Producer = cms.required.InputTag
    )
  ),
  VSallWP = cms.vstring('0'),
  mightGet = cms.optional.untracked.vstring
)
