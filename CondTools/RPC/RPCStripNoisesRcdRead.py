import FWCore.ParameterSet.Config as cms

def RPCStripNoisesRcdRead(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCStripNoisesRcdRead',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
