import FWCore.ParameterSet.Config as cms

def L1GTAlgoBlockProducer(**kwargs):
  mod = cms.EDProducer('L1GTAlgoBlockProducer',
    algorithms = cms.required.VPSet,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
