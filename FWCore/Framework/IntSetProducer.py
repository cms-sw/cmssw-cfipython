import FWCore.ParameterSet.Config as cms

def IntSetProducer(*args, **kwargs):
  mod = cms.EDProducer('IntSetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
