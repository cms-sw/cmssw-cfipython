import FWCore.ParameterSet.Config as cms

def MuEnrichRenormalizer(**kwargs):
  mod = cms.EDAnalyzer('MuEnrichRenormalizer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
