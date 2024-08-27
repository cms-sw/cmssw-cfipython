import FWCore.ParameterSet.Config as cms

def Mixing2DB(**kwargs):
  mod = cms.EDAnalyzer('Mixing2DB',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
