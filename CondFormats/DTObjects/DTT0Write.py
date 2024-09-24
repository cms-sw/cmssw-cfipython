import FWCore.ParameterSet.Config as cms

def DTT0Write(**kwargs):
  mod = cms.EDAnalyzer('DTT0Write',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod