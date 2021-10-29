import FWCore.ParameterSet.Config as cms

deepMETProducer = cms.EDProducer('DeepMETProducer',
  pf_src = cms.InputTag('packedPFCandidates'),
  ignore_leptons = cms.bool(False),
  norm_factor = cms.double(50),
  max_n_pf = cms.uint32(4500),
  graph_path = cms.string('RecoMET/METPUSubtraction/data/deepmet/deepmet_v1_2018.pb'),
  mightGet = cms.optional.untracked.vstring
)
