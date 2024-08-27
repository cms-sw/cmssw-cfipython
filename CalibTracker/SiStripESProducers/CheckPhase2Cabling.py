import FWCore.ParameterSet.Config as cms

def CheckPhase2Cabling(**kwargs):
  mod = cms.EDAnalyzer('CheckPhase2Cabling',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
