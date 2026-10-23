import FWCore.ParameterSet.Config as cms

def RPCDCSSummary(*args, **kwargs):
  mod = cms.EDProducer('RPCDCSSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
