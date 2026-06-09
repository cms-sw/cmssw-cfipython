import FWCore.ParameterSet.Config as cms

def HLTTauRefCombiner(*args, **kwargs):
  mod = cms.EDProducer('HLTTauRefCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
