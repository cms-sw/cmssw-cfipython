import FWCore.ParameterSet.Config as cms

def CTPPSAlignmentInfo(*args, **kwargs):
  mod = cms.EDAnalyzer('CTPPSAlignmentInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
