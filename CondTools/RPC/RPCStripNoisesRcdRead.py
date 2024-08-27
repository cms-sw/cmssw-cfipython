import FWCore.ParameterSet.Config as cms

def RPCStripNoisesRcdRead(**kwargs):
  mod = cms.EDAnalyzer('RPCStripNoisesRcdRead',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
