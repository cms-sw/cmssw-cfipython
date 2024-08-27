import FWCore.ParameterSet.Config as cms

def CSCViewDigi(**kwargs):
  mod = cms.EDAnalyzer('CSCViewDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
