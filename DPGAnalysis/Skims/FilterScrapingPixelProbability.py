import FWCore.ParameterSet.Config as cms

def FilterScrapingPixelProbability(*args, **kwargs):
  mod = cms.EDFilter('FilterScrapingPixelProbability',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
