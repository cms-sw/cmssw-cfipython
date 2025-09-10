import FWCore.ParameterSet.Config as cms

def UseValueExampleAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('UseValueExampleAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
