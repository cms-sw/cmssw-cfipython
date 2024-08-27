import FWCore.ParameterSet.Config as cms

def CandPtIsolationProducer(**kwargs):
  mod = cms.EDProducer('CandPtIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
