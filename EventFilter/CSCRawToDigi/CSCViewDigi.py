import FWCore.ParameterSet.Config as cms

def CSCViewDigi(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCViewDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
