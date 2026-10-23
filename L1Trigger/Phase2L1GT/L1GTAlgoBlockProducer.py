import FWCore.ParameterSet.Config as cms

def L1GTAlgoBlockProducer(*args, **kwargs):
  mod = cms.EDProducer('L1GTAlgoBlockProducer',
    algorithms = cms.required.VPSet,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
