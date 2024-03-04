import FWCore.ParameterSet.Config as cms

def DBReader(**kwargs):
  mod = cms.EDAnalyzer('DBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
