import FWCore.ParameterSet.Config as cms

def IntVectorSetProducer(**kwargs):
  mod = cms.EDProducer('IntVectorSetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
