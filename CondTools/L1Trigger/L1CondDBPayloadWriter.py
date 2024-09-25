import FWCore.ParameterSet.Config as cms

def L1CondDBPayloadWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('L1CondDBPayloadWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
