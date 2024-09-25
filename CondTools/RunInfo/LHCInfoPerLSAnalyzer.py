import FWCore.ParameterSet.Config as cms

def LHCInfoPerLSAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('LHCInfoPerLSAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
