import FWCore.ParameterSet.Config as cms

def RetrievePPSAlignmentConfiguration(*args, **kwargs):
  mod = cms.EDAnalyzer('RetrievePPSAlignmentConfiguration',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
