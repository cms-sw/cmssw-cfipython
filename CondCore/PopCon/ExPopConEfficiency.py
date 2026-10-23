import FWCore.ParameterSet.Config as cms

def ExPopConEfficiency(*args, **kwargs):
  mod = cms.EDAnalyzer('ExPopConEfficiency',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
