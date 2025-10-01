import FWCore.ParameterSet.Config as cms

def L1TZDCEtSumsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('L1TZDCEtSumsAnalyzer',
    etSumTag = cms.InputTag('l1tZDCEtSums'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
