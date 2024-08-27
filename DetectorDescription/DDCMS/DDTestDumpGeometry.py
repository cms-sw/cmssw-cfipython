import FWCore.ParameterSet.Config as cms

def DDTestDumpGeometry(**kwargs):
  mod = cms.EDAnalyzer('DDTestDumpGeometry',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
