import FWCore.ParameterSet.Config as cms

def PathStateRelease(*args, **kwargs):
  mod = cms.EDFilter('PathStateRelease',
    state = cms.InputTag('pathStateCapture'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
