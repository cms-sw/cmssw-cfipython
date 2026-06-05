import FWCore.ParameterSet.Config as cms

def WriteTotemDAQMapping(*args, **kwargs):
  mod = cms.EDAnalyzer('WriteTotemDAQMapping',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
