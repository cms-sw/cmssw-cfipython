import FWCore.ParameterSet.Config as cms

def PythiaFilterZJetWithOutBg(*args, **kwargs):
  mod = cms.EDFilter('PythiaFilterZJetWithOutBg',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
