import FWCore.ParameterSet.Config as cms

def ProbeTreeProducer(**kwargs):
  mod = cms.EDFilter('ProbeTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
