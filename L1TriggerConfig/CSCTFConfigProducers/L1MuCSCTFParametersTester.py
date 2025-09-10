import FWCore.ParameterSet.Config as cms

def L1MuCSCTFParametersTester(*args, **kwargs):
  mod = cms.EDAnalyzer('L1MuCSCTFParametersTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
