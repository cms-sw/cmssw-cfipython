import FWCore.ParameterSet.Config as cms

def DTSpyReader(*args, **kwargs):
  mod = cms.EDProducer('DTSpyReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
