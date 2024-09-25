import FWCore.ParameterSet.Config as cms

def L1TCSCTF(*args, **kwargs):
  mod = cms.EDProducer('L1TCSCTF',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
