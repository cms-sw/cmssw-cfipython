import FWCore.ParameterSet.Config as cms

def CSCFileDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCFileDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
