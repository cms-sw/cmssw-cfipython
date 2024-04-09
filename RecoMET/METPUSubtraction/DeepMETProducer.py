import FWCore.ParameterSet.Config as cms

def DeepMETProducer(**kwargs):
  mod = cms.EDProducer('DeepMETProducer',
    pf_src = cms.InputTag('packedPFCandidates'),
    ignore_leptons = cms.bool(False),
    norm_factor = cms.double(50),
    max_n_pf = cms.uint32(4500),
    graph_path = cms.string('RecoMET/METPUSubtraction/data/models/deepmet/deepmet_v1_2018/model.graphdef'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod