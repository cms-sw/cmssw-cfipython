import FWCore.ParameterSet.Config as cms

def GenMETShallowCloneProducer(**kwargs):
  mod = cms.EDProducer('GenMETShallowCloneProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
