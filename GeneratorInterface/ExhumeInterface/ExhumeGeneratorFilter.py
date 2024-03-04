import FWCore.ParameterSet.Config as cms

def ExhumeGeneratorFilter(**kwargs):
  mod = cms.EDFilter('ExhumeGeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
