import FWCore.ParameterSet.Config as cms

def KVFTrackUpdate(*args, **kwargs):
  mod = cms.EDAnalyzer('KVFTrackUpdate',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
