import FWCore.ParameterSet.Config as cms

def AlignmentRcdChecker(**kwargs):
  mod = cms.EDAnalyzer('AlignmentRcdChecker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
