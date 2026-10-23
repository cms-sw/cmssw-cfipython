import FWCore.ParameterSet.Config as cms

def PATMETSlimmer(*args, **kwargs):
  mod = cms.EDProducer('PATMETSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
