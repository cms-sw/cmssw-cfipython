import FWCore.ParameterSet.Config as cms

def PythiaFilterZJet(**kwargs):
  mod = cms.EDFilter('PythiaFilterZJet',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
