import FWCore.ParameterSet.Config as cms

def PhysicsPerformanceDBWriterFromFile_WPandPayload_IOV(*args, **kwargs):
  mod = cms.EDAnalyzer('PhysicsPerformanceDBWriterFromFile_WPandPayload_IOV',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
