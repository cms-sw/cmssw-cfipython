import FWCore.ParameterSet.Config as cms

def FillInfoESAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('FillInfoESAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
