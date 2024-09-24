import FWCore.ParameterSet.Config as cms

def L1HOTreeProducer(**kwargs):
  mod = cms.EDAnalyzer('L1HOTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod