import FWCore.ParameterSet.Config as cms

def IntVecRefVectorProducer(*args, **kwargs):
  mod = cms.EDProducer('IntVecRefVectorProducer',
    select = cms.int32(0),
    target = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
