import FWCore.ParameterSet.Config as cms

def edm_test_cpu_IntProducer(**kwargs):
  mod = cms.EDProducer('edm::test::cpu::IntProducer',
    valueOther = cms.required.int32,
    valueCpu = cms.required.int32,
    variant = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
