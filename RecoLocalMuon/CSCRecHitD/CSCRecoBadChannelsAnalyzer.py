import FWCore.ParameterSet.Config as cms

def CSCRecoBadChannelsAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCRecoBadChannelsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
