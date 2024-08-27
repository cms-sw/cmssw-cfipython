import FWCore.ParameterSet.Config as cms

def ttHFGenFilter(**kwargs):
  mod = cms.EDFilter('ttHFGenFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
