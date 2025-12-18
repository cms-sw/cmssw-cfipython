import FWCore.ParameterSet.Config as cms

def CFWriter(*args, **kwargs):
  mod = cms.EDProducer('CFWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
