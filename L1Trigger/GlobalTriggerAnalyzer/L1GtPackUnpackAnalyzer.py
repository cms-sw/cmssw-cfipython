import FWCore.ParameterSet.Config as cms

def L1GtPackUnpackAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('L1GtPackUnpackAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
