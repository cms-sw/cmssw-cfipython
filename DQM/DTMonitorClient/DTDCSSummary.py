import FWCore.ParameterSet.Config as cms

def DTDCSSummary(**kwargs):
  mod = cms.EDProducer('DTDCSSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
