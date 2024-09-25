import FWCore.ParameterSet.Config as cms

def GEMCSCLUTAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('GEMCSCLUTAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
