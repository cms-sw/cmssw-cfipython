import FWCore.ParameterSet.Config as cms

def IntVecStdVectorPtrProducer(**kwargs):
  mod = cms.EDProducer('IntVecStdVectorPtrProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
