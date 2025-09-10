import FWCore.ParameterSet.Config as cms

def MuonTimingValidator(*args, **kwargs):
  mod = cms.EDAnalyzer('MuonTimingValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
