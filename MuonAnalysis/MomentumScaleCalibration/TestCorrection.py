import FWCore.ParameterSet.Config as cms

def TestCorrection(**kwargs):
  mod = cms.EDAnalyzer('TestCorrection',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
