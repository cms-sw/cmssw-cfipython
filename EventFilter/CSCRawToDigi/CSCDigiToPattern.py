import FWCore.ParameterSet.Config as cms

def CSCDigiToPattern(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCDigiToPattern',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
