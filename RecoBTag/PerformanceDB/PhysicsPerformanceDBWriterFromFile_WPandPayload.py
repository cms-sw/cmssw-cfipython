import FWCore.ParameterSet.Config as cms

def PhysicsPerformanceDBWriterFromFile_WPandPayload(**kwargs):
  mod = cms.EDAnalyzer('PhysicsPerformanceDBWriterFromFile_WPandPayload',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
