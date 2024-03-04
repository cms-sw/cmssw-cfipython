import FWCore.ParameterSet.Config as cms

def CleanAndMergeProducer(**kwargs):
  mod = cms.EDProducer('CleanAndMergeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
