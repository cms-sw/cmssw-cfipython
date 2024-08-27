import FWCore.ParameterSet.Config as cms

def PhysicsPerformanceDBWriterTFormula_fromfile_WPandPL(**kwargs):
  mod = cms.EDAnalyzer('PhysicsPerformanceDBWriterTFormula_fromfile_WPandPL',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
