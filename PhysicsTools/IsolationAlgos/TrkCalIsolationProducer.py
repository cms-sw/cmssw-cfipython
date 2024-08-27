import FWCore.ParameterSet.Config as cms

def TrkCalIsolationProducer(**kwargs):
  mod = cms.EDProducer('TrkCalIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
