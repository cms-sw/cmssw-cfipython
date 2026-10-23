import FWCore.ParameterSet.Config as cms

def PhysicsPerformanceDBWriterTFormula_fromfile_WPandPL(*args, **kwargs):
  mod = cms.EDAnalyzer('PhysicsPerformanceDBWriterTFormula_fromfile_WPandPL',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
