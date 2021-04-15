import FWCore.ParameterSet.Config as cms

mlpfProducer = cms.EDProducer('MLPFProducer',
  src = cms.InputTag('particleFlowBlock'),
  model_path = cms.string('RecoParticleFlow/PFProducer/data/mlpf/mlpf_2020_11_04.pb'),
  mightGet = cms.optional.untracked.vstring
)
