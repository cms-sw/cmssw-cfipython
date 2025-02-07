import FWCore.ParameterSet.Config as cms

def AlignmentMonitorAsAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('AlignmentMonitorAsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
