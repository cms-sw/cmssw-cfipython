import FWCore.ParameterSet.Config as cms

def CondReader(**kwargs):
  mod = cms.EDAnalyzer('CondReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
