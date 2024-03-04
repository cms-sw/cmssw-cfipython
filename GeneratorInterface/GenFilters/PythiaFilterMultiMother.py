import FWCore.ParameterSet.Config as cms

def PythiaFilterMultiMother(**kwargs):
  mod = cms.EDFilter('PythiaFilterMultiMother',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
