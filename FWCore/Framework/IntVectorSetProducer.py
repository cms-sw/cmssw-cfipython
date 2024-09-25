import FWCore.ParameterSet.Config as cms

def IntVectorSetProducer(*args, **kwargs):
  mod = cms.EDProducer('IntVectorSetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
