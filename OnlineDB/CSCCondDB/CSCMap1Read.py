import FWCore.ParameterSet.Config as cms

def CSCMap1Read(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCMap1Read',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
