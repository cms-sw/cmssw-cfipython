import FWCore.ParameterSet.Config as cms

def TestWriteESAlignments(**kwargs):
  mod = cms.EDAnalyzer('TestWriteESAlignments',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
