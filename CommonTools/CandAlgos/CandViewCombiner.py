import FWCore.ParameterSet.Config as cms

def CandViewCombiner(*args, **kwargs):
  mod = cms.EDProducer('CandViewCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
