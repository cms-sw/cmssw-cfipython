import FWCore.ParameterSet.Config as cms

def BTLRecoSoADump(*args, **kwargs):
  mod = cms.EDAnalyzer('BTLRecoSoADump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
