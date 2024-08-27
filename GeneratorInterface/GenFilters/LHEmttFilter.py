import FWCore.ParameterSet.Config as cms

def LHEmttFilter(**kwargs):
  mod = cms.EDFilter('LHEmttFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
