import FWCore.ParameterSet.Config as cms

def IntVecRefToBaseVectorProducer(**kwargs):
  mod = cms.EDProducer('IntVecRefToBaseVectorProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
