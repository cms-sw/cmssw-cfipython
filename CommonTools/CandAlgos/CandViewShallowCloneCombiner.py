import FWCore.ParameterSet.Config as cms

def CandViewShallowCloneCombiner(*args, **kwargs):
  mod = cms.EDProducer('CandViewShallowCloneCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
