import FWCore.ParameterSet.Config as cms

def L1TdeCSCTPG(*args, **kwargs):
  mod = cms.EDProducer('L1TdeCSCTPG',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
