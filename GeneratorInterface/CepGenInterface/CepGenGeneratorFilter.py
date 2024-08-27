import FWCore.ParameterSet.Config as cms

def CepGenGeneratorFilter(**kwargs):
  mod = cms.EDFilter('CepGenGeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
