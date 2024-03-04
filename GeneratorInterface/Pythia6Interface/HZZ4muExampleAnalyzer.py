import FWCore.ParameterSet.Config as cms

def HZZ4muExampleAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HZZ4muExampleAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
