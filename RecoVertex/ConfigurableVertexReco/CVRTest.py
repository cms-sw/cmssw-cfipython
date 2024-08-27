import FWCore.ParameterSet.Config as cms

def CVRTest(**kwargs):
  mod = cms.EDAnalyzer('CVRTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
