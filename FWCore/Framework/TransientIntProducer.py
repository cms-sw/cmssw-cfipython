import FWCore.ParameterSet.Config as cms

def TransientIntProducer(*args, **kwargs):
  mod = cms.EDProducer('TransientIntProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
