import FWCore.ParameterSet.Config as cms

def DTDCSByLumiSummary(**kwargs):
  mod = cms.EDProducer('DTDCSByLumiSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
