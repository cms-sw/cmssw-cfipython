import FWCore.ParameterSet.Config as cms

def RetrieveCTPPSRPAlignmentCorrectionsData(*args, **kwargs):
  mod = cms.EDAnalyzer('RetrieveCTPPSRPAlignmentCorrectionsData',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
