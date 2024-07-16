import FWCore.ParameterSet.Config as cms

def L1AXOTreeProducer(**kwargs):
  mod = cms.EDAnalyzer('L1AXOTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
