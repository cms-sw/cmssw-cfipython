import FWCore.ParameterSet.Config as cms

def ETLRecoSoADump(*args, **kwargs):
  mod = cms.EDAnalyzer('ETLRecoSoADump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
