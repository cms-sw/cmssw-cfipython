import FWCore.ParameterSet.Config as cms

def CleanAndMergeProducer(*args, **kwargs):
  mod = cms.EDProducer('CleanAndMergeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
