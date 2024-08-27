import FWCore.ParameterSet.Config as cms

def L1uGTTreeProducer(**kwargs):
  mod = cms.EDAnalyzer('L1uGTTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
