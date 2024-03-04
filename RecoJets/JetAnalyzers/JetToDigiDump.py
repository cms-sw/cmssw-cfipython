import FWCore.ParameterSet.Config as cms

def JetToDigiDump(**kwargs):
  mod = cms.EDAnalyzer('JetToDigiDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
