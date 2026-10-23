import FWCore.ParameterSet.Config as cms

def CSCTightHalo2015Filter(*args, **kwargs):
  mod = cms.EDFilter('CSCTightHalo2015Filter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
