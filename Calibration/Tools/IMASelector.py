import FWCore.ParameterSet.Config as cms

def IMASelector(**kwargs):
  mod = cms.EDFilter('IMASelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
