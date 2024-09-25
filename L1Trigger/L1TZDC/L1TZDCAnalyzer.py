import FWCore.ParameterSet.Config as cms

def L1TZDCAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TZDCAnalyzer',
    etSumTag = cms.InputTag('l1tZDCEtSums'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
