import FWCore.ParameterSet.Config as cms

def SimpleJetDump(**kwargs):
  mod = cms.EDAnalyzer('SimpleJetDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
