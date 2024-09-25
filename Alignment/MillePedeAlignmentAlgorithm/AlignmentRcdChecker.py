import FWCore.ParameterSet.Config as cms

def AlignmentRcdChecker(*args, **kwargs):
  mod = cms.EDAnalyzer('AlignmentRcdChecker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
