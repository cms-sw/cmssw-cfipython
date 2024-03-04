import FWCore.ParameterSet.Config as cms

def DeleteEarlyRefProdReader(**kwargs):
  mod = cms.EDAnalyzer('DeleteEarlyRefProdReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
