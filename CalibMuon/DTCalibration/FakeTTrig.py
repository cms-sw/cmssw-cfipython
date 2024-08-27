import FWCore.ParameterSet.Config as cms

def FakeTTrig(**kwargs):
  mod = cms.EDAnalyzer('FakeTTrig',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
