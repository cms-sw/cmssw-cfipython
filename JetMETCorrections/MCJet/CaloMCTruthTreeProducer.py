import FWCore.ParameterSet.Config as cms

def CaloMCTruthTreeProducer(**kwargs):
  mod = cms.EDAnalyzer('CaloMCTruthTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
