import FWCore.ParameterSet.Config as cms

def DTPtaLutTester(**kwargs):
  mod = cms.EDAnalyzer('DTPtaLutTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
