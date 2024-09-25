import FWCore.ParameterSet.Config as cms

def TestWriteESAlignments(*args, **kwargs):
  mod = cms.EDAnalyzer('TestWriteESAlignments',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
