import FWCore.ParameterSet.Config as cms

def CandViewShallowClonePtrCombiner(*args, **kwargs):
  mod = cms.EDProducer('CandViewShallowClonePtrCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
