import FWCore.ParameterSet.Config as cms

def QcdHighPtDQM(*args, **kwargs):
  mod = cms.EDProducer('QcdHighPtDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
