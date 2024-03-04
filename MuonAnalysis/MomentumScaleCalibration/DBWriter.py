import FWCore.ParameterSet.Config as cms

def DBWriter(**kwargs):
  mod = cms.EDAnalyzer('DBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
