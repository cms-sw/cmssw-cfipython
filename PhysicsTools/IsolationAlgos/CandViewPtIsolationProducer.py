import FWCore.ParameterSet.Config as cms

def CandViewPtIsolationProducer(**kwargs):
  mod = cms.EDProducer('CandViewPtIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
