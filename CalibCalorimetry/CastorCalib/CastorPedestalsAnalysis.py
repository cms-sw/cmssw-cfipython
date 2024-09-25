import FWCore.ParameterSet.Config as cms

def CastorPedestalsAnalysis(*args, **kwargs):
  mod = cms.EDAnalyzer('CastorPedestalsAnalysis',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
