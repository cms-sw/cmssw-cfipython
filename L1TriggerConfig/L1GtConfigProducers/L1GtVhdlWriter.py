import FWCore.ParameterSet.Config as cms

def L1GtVhdlWriter(**kwargs):
  mod = cms.EDAnalyzer('L1GtVhdlWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
