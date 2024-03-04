import FWCore.ParameterSet.Config as cms

def PATMETRefSelector(**kwargs):
  mod = cms.EDFilter('PATMETRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
