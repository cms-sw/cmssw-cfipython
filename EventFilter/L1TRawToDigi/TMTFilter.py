import FWCore.ParameterSet.Config as cms

def TMTFilter(**kwargs):
  mod = cms.EDFilter('TMTFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
