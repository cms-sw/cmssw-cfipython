import FWCore.ParameterSet.Config as cms

def RctDigiToRctText(**kwargs):
  mod = cms.EDAnalyzer('RctDigiToRctText',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
