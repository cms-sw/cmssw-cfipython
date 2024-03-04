import FWCore.ParameterSet.Config as cms

def IntVecRefVectorProducer(**kwargs):
  mod = cms.EDProducer('IntVecRefVectorProducer',
    select = cms.int32(0),
    target = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
