import FWCore.ParameterSet.Config as cms

def CTPPSRPAlignmentInfoAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CTPPSRPAlignmentInfoAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
