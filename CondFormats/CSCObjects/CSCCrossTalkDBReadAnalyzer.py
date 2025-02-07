import FWCore.ParameterSet.Config as cms

def CSCCrossTalkDBReadAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCCrossTalkDBReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
