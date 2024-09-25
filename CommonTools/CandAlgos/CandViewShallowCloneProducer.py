import FWCore.ParameterSet.Config as cms

def CandViewShallowCloneProducer(*args, **kwargs):
  mod = cms.EDFilter('CandViewShallowCloneProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
