import FWCore.ParameterSet.Config as cms

def ConsumingIntProducer(*args, **kwargs):
  mod = cms.EDProducer('ConsumingIntProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
