import FWCore.ParameterSet.Config as cms

def AlignmentRcdScan(*args, **kwargs):
  mod = cms.EDAnalyzer('AlignmentRcdScan',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
