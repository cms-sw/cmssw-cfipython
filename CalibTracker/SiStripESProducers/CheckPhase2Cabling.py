import FWCore.ParameterSet.Config as cms

def CheckPhase2Cabling(*args, **kwargs):
  mod = cms.EDAnalyzer('CheckPhase2Cabling',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
