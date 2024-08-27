import FWCore.ParameterSet.Config as cms

def ClassifierMerger(**kwargs):
  mod = cms.EDProducer('ClassifierMerger',
    inputClassifiers = cms.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
