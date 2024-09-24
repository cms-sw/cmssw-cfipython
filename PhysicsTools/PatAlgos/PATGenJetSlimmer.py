import FWCore.ParameterSet.Config as cms

def PATGenJetSlimmer(*args, **kwargs):
  mod = cms.EDProducer('PATGenJetSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
