import FWCore.ParameterSet.Config as cms

def PATJetSlimmer(*args, **kwargs):
  mod = cms.EDProducer('PATJetSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
