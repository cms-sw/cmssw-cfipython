import FWCore.ParameterSet.Config as cms

def TestRandomNumberServiceGlobal(**kwargs):
  mod = cms.EDAnalyzer('TestRandomNumberServiceGlobal',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
