import FWCore.ParameterSet.Config as cms

def QcdLowPtDQM(*args, **kwargs):
  mod = cms.EDProducer('QcdLowPtDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
