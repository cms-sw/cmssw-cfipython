import FWCore.ParameterSet.Config as cms

def PseudoTopProducer(*args, **kwargs):
  mod = cms.EDProducer('PseudoTopProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
