import FWCore.ParameterSet.Config as cms

def edm_test_cpu_IntTransformer(**kwargs):
  mod = cms.EDProducer('edm::test::cpu::IntTransformer',
    valueOther = cms.required.int32,
    valueCpu = cms.required.int32,
    variant = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
