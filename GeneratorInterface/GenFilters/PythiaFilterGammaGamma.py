import FWCore.ParameterSet.Config as cms

def PythiaFilterGammaGamma(*args, **kwargs):
  mod = cms.EDFilter('PythiaFilterGammaGamma',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
