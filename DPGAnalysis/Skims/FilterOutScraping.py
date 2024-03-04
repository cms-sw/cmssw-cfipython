import FWCore.ParameterSet.Config as cms

def FilterOutScraping(**kwargs):
  mod = cms.EDFilter('FilterOutScraping',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
