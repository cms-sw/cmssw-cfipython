import FWCore.ParameterSet.Config as cms

def PythiaFilterGammaJetWithBg(*args, **kwargs):
  mod = cms.EDFilter('PythiaFilterGammaJetWithBg',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
