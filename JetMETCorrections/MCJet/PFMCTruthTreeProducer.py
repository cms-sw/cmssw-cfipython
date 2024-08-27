import FWCore.ParameterSet.Config as cms

def PFMCTruthTreeProducer(**kwargs):
  mod = cms.EDAnalyzer('PFMCTruthTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
