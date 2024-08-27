import FWCore.ParameterSet.Config as cms

def AlignmentMonitorAsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('AlignmentMonitorAsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
