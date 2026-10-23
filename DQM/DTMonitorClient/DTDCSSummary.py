import FWCore.ParameterSet.Config as cms

def DTDCSSummary(*args, **kwargs):
  mod = cms.EDProducer('DTDCSSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
