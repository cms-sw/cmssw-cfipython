import FWCore.ParameterSet.Config as cms

def DeleteEarlyCheckDeleteAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DeleteEarlyCheckDeleteAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
