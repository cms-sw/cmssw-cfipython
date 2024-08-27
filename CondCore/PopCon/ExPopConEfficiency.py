import FWCore.ParameterSet.Config as cms

def ExPopConEfficiency(**kwargs):
  mod = cms.EDAnalyzer('ExPopConEfficiency',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
