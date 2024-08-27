import FWCore.ParameterSet.Config as cms

def HistProducer(**kwargs):
  mod = cms.EDProducer('HistProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
