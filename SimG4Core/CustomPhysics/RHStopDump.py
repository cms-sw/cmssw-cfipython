import FWCore.ParameterSet.Config as cms

def RHStopDump(*args, **kwargs):
  mod = cms.EDAnalyzer('RHStopDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
