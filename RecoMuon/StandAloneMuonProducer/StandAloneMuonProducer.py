import FWCore.ParameterSet.Config as cms

def StandAloneMuonProducer(*args, **kwargs):
  mod = cms.EDProducer('StandAloneMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
