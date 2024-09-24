import FWCore.ParameterSet.Config as cms

def DTDCSByLumiSummary(*args, **kwargs):
  mod = cms.EDProducer('DTDCSByLumiSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
