import FWCore.ParameterSet.Config as cms

def L1GctInternJetProducer(*args, **kwargs):
  mod = cms.EDProducer('L1GctInternJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
