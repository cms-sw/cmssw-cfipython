import FWCore.ParameterSet.Config as cms

def PythiaFilterZJetWithOutBg(**kwargs):
  mod = cms.EDFilter('PythiaFilterZJetWithOutBg',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
