import FWCore.ParameterSet.Config as cms

def CSCGainsReadAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCGainsReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
