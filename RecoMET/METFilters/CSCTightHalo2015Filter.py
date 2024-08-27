import FWCore.ParameterSet.Config as cms

def CSCTightHalo2015Filter(**kwargs):
  mod = cms.EDFilter('CSCTightHalo2015Filter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
