import FWCore.ParameterSet.Config as cms

def ptHatFilter(**kwargs):
  mod = cms.EDFilter('ptHatFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
