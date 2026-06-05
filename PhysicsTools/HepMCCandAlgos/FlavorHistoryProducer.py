import FWCore.ParameterSet.Config as cms

def FlavorHistoryProducer(*args, **kwargs):
  mod = cms.EDProducer('FlavorHistoryProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
