import FWCore.ParameterSet.Config as cms

def CSCFileDumper(**kwargs):
  mod = cms.EDAnalyzer('CSCFileDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
