import FWCore.ParameterSet.Config as cms

def TestLumiCorrectionSource(*args, **kwargs):
  mod = cms.EDAnalyzer('TestLumiCorrectionSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
