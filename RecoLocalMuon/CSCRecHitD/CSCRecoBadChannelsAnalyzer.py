import FWCore.ParameterSet.Config as cms

def CSCRecoBadChannelsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCRecoBadChannelsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
