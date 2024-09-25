import FWCore.ParameterSet.Config as cms

def L1TdeCSCTPGClient(*args, **kwargs):
  mod = cms.EDProducer('L1TdeCSCTPGClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
