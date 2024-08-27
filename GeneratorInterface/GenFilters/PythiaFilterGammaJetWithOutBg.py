import FWCore.ParameterSet.Config as cms

def PythiaFilterGammaJetWithOutBg(**kwargs):
  mod = cms.EDFilter('PythiaFilterGammaJetWithOutBg',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
