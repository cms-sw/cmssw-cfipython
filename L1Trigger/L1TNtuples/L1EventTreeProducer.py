import FWCore.ParameterSet.Config as cms

def L1EventTreeProducer(**kwargs):
  mod = cms.EDAnalyzer('L1EventTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
