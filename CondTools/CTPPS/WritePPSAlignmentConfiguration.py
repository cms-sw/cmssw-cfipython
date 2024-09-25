import FWCore.ParameterSet.Config as cms

def WritePPSAlignmentConfiguration(*args, **kwargs):
  mod = cms.EDAnalyzer('WritePPSAlignmentConfiguration',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
