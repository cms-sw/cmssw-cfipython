import FWCore.ParameterSet.Config as cms

def FilterScrapingPixelProbability(**kwargs):
  mod = cms.EDFilter('FilterScrapingPixelProbability',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
