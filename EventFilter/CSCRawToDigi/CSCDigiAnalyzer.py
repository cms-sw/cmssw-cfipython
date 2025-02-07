import FWCore.ParameterSet.Config as cms

def CSCDigiAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCDigiAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
