import FWCore.ParameterSet.Config as cms

def Compare(*args, **kwargs):
  mod = cms.EDAnalyzer('Compare',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
