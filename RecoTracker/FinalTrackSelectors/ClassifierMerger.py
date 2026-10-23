import FWCore.ParameterSet.Config as cms

def ClassifierMerger(*args, **kwargs):
  mod = cms.EDProducer('ClassifierMerger',
    inputClassifiers = cms.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
