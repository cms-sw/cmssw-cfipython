import FWCore.ParameterSet.Config as cms

def PATPhotonRefSelector(**kwargs):
  mod = cms.EDFilter('PATPhotonRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
