import FWCore.ParameterSet.Config as cms

def CSCGainsStudy(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCGainsStudy',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
