import FWCore.ParameterSet.Config as cms

def RPCDCSSummary(**kwargs):
  mod = cms.EDProducer('RPCDCSSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
