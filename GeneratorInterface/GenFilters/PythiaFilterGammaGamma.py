import FWCore.ParameterSet.Config as cms

def PythiaFilterGammaGamma(**kwargs):
  mod = cms.EDFilter('PythiaFilterGammaGamma',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
