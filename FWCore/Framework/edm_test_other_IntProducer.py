import FWCore.ParameterSet.Config as cms

def edm_test_other_IntProducer(*args, **kwargs):
  mod = cms.EDProducer('edm::test::other::IntProducer',
    valueOther = cms.required.int32,
    valueCpu = cms.required.int32,
    variant = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
