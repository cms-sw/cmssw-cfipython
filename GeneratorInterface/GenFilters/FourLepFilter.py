import FWCore.ParameterSet.Config as cms

def FourLepFilter(**kwargs):
  mod = cms.EDFilter('FourLepFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
