import FWCore.ParameterSet.Config as cms

def RHStopDump(**kwargs):
  mod = cms.EDAnalyzer('RHStopDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
