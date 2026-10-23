import FWCore.ParameterSet.Config as cms

def PATTauSlimmer(*args, **kwargs):
  mod = cms.EDProducer('PATTauSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
