import FWCore.ParameterSet.Config as cms

def PythiaFilterGammaJet(**kwargs):
  mod = cms.EDFilter('PythiaFilterGammaJet',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
