import FWCore.ParameterSet.Config as cms

def DQMHOAlCaRecoStream(**kwargs):
  mod = cms.EDProducer('DQMHOAlCaRecoStream',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
