import FWCore.ParameterSet.Config as cms

def NamedCandViewCombiner(*args, **kwargs):
  mod = cms.EDProducer('NamedCandViewCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
